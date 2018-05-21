import json

def read_json(fn):
    with open(fn,'r') as f:
        return json.load(f)

def write_json(fn,data):
    with open(fn,'w') as f:
        json.dump(data, f, indent=2)
