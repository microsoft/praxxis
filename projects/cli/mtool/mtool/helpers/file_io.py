import json

def load_json(filename):
    with open(filename, encoding="utf8") as json_file:
        return json.load(json_file)

def save_json(filename, contents):
    with open(filename, 'w', encoding="utf8") as outfile:
        json.dump(contents, outfile, indent=4)