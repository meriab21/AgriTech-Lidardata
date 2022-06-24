# AgriTech-Lidardata.
In this project we are exploring data from USGS_3DEP ( United States Geological Survey 3D Elevation Program).  


## Table of Content

- [Introduction](#introduction)
- [Install](#instalation)
- [Technologies used](#technologies-used)
- [Data](#data)
- [Notebooks](#notebooks)
- [Scripts](#scripts)
- [Test](#test)

### Introduction

AgriTech is concerned with how water flows through a maize farm field as this knowlege will help improve research on new agricultural products being tested on the farm. The main project in this project is to produce an easy to use, reliable and well designed python module that domain experts and data scientists can use to fetch, visualise, and transform publicly available satellite and LIDAR data. In particular, your code should interface with USGS 3DEP and fetch data using their API.
### Installation

- **Set up**

```
git clone https://github.com/meriab21/AgriTech-Lidardata
cd AgriTech-Lidardata
pip install -r requirements.txt
```
### Technologies used

- PDAL
- Geopandas

### Data

- The Data: is a LIDAR HIgh definition elevation data. It is a point cloud, which is basically a set of data points in space. The points may represent a 3D shape or object. Each point position has its set of Cartesian coordinates (X, Y, Z) and associated characteristics like intensity, color, and many others. In the context of this project, the data is a national baseline of consistent high-resolution topographic elevation data – both bare earth and 3D point clouds collected in the 3D Elevation Program led by USGS.

- Source of data: USGS uploaded publicly available amazon s3 bucket found in the following url https://s3-us-west-2.amazonaws.com/usgs-lidar-public.

### Notebooks
All the analysis on the data done one the juputer notebook are done
### Scripts
All scripts for the analysis will be found here
### Test

All tests will be found here
