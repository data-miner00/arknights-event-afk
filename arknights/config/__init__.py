import json


class Configurations:
    configurations: dict

    def __init__(self):
        with open("settings.json", "r") as f:
            self.configurations = json.load(f)

    def read_settings(self, key: str):
        return self.configurations[key]
