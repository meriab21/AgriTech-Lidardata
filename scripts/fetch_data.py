import logging
import sys
import pdal
import pandas as pd
import json
import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon, Point, mapping
import numpy as np
from pyproj import Proj, transform
import folium
import laspy as lp
import richdem as rd
import rasterio
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import logging
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# importing scripts
sys.path.insert(1, '..')
sys.path.append("..")
sys.path.append(".")


class DataLoading:
    """
    class that handles data cleaning.
    """

    def __init__(self, filehandler) -> None:
        file_handler = logging.FileHandler(filehandler)
        formatter = logging.Formatter(
            "time: %(asctime)s, function: %(funcName)s, module: %(name)s, message: %(message)s \n")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # loading and reading json file
    def read_json(json_path):
        try:
            with open(json_path) as json_file:
                data = json.load(json_file)
                return data
        except FileNotFoundError:
            print("File not found")
            return None
        
    # Creating a function to change to the needed CRS format for better visualization
    """        parameters
        fromT: the original EPSG format
        lon: the longitude value
        lat: the latitude value
    """
    def convert_EPSG(fromT, lon, lat):
        P3857 = Proj(init='epsg:3857')
        P4326 = Proj(init='epsg:4326')
        if(fromT == 4326):
            input1 = P4326
            input2 = P3857
        else:
            input1 = p3857
            input2 = p4326

        x, y = transform(input1, input2, lon, lat)
        return [x, y]
    # [x, y]: a list with new EPSG formatted values

    # A function to change format of a list of coordinates to a list of points
    def loop_EPSG_converter(listin):
        converted = []
        for item in listin:
            converted.append(convert_EPSG(4326, item[0], item[1]))

        return converted

    def generate_polygon(coor, epsg):
        polygon_g = Polygon(coor)
        crs = {'init': 'epsg:'+str(epsg)}
        polygon = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[polygon_g])
        return polygon

    # generating a dataframe given a CRS format and pipe
    def generate_geo_df(pipe, epsg):
        try:
            cloud_points = []
            elevations = []
            geometry_points = []
            for row in pipe.arrays[0]:
                lst = row.tolist()[-3:]
                cloud_points.append(lst)
                elevations.append(lst[2])
                point = Point(lst[0], lst[1])
                geometry_points.append(point)
            geodf = gpd.GeoDataFrame(columns=["elevation", "geometry"])
            geodf['elevation'] = elevations
            geodf['geometry'] = geometry_points
            geodf = geodf.set_geometry("geometry")
            geodf.set_crs(epsg=epsg, inplace=True)
            return geodf
        except RuntimeError as e:
            print(e)

    # A function to display the polygon on a map
    def show_on_map(polygon, zoom):
        # region selection
        poly = mapping((polygon.iloc[:, 0][0]))
        tmp = poly['coordinates'][0][0]
        anchor = [tmp[1], tmp[0]]
        map = folium.Map(anchor, zoom_start=zoom, tiles='cartodbpositron')
        folium.GeoJson(polygon).add_to(map)
        folium.LatLngPopup().add_to(map)
        return map

    # Modifying the already created json file to fetch the data

    def modify_pipe_json(json_loc, url, region, in_epsg, out_epsg):
        dicti = read_json(json_loc)
        dicti['pipeline'][0]['polygon'] = str(polygon_standard.iloc[:, 0][0])
        dicti['pipeline'][0]['filename'] = f"{url}/{region}/ept.json"
        dicti['pipeline'][2]['in_srs'] = f"EPSG:{in_epsg}"
        dicti['pipeline'][2]['out_srs'] = f"EPSG:{out_epsg}"
        print(dicti)
        return dicti


    # plotting the elevation graph
    def plot_elevation(df):
        #plotting the elevation graph
        df.plot(c='elevation', cmap='terrain')
        plt.title('Terrain Elevation') 
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')

    def read_las(las_file):
        las = lp.read(las_file)
        return las
        logger.info("succesfully read from las file")
