import json

def load_forecast(path):
    with open(path, "r") as f:
        return json.load(f)
