import json
from pprint import pprint

# take in the city.list.json and return the appropriate data


# opens a json file and returns it
def load_json():
    with open('city.list.json') as f:
        data = json.load(f)
        return data


# takes in json and returns json sorted on name which is the key we have here speciefied
def sort_json(json):
    dict = {}
    dict.setdefault('key_name', []).append('value')
    for data in json:
        data.pop('coord', None)
        prefix = ""
        if len(data['name']) > 0:
            prefix = data['name'][0]
        else:
            prefix = ' '
        if dict.get(prefix):
            dict[prefix].append(data)
        else:
            dict[prefix] = [data]
    return dict


# write the sorted file to a json file
def write_to_file(data):
    with open('alphabeticSortedJson.json', 'w+') as h:
        json.dump(data, h, indent=4)


data = load_json()
sorted_json = sort_json(data)
write_to_file(sorted_json)



