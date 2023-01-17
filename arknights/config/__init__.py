import json


def read_settings() -> dict:
    with open("settings.json", "r") as f:
        return json.load(f)
