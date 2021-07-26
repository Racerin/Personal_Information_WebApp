import os, json, time
from dataclasses import dataclass


@dataclass
class JsonDatabase():
    json_file_name : str = "json info.json"
    json_obj = dict()

    def __init__(self):
        """Load dict from json file"""
        self.load_json_file()

    #Context Manager Dunder Methods
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.save_json_file()

    def recall(self, key, default=dict()):
        """Returns Json object if exists, else returns the type of the object"""
        try:
            return self.json_obj[key]
        except KeyError:
            return default

    def submit(self, key, val):
        self.json_obj[key] = val

    def load_json_file(self):
        """Assign json object of file to 'json_obj'. """
        if not os.path.exists(self.json_file_name):
            #Create file and object
            self.save_json_file()
        else:
            ##Retrieve the file
            with open(self.json_file_name) as file:
                self.json_obj = json.load(file)

    def save_json_file(self):
        with open(self.json_file_name, mode="w+") as file:
            json.dump(self.json_obj, file)
