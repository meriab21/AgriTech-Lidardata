#loading and reading json file
def read_json(json_path):
    try:
        with open(json_path) as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print("File not found")
        return None