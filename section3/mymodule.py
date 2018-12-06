import json
fname = 'jawiki-country.json'

def extract_text(title):
    with open(fname) as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == title:
                return data_json['text']
