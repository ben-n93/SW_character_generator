import json

import requests

def API_scrape(resource, property):
    """ Call the SWAPI and create a list of data. """
    data_list = []
    for number in range(1, 30):
        response = requests.get(f"https://swapi.dev/api/{resource}/?page={number}")
        if response.status_code != 200:
            continue
        else:
            data = response.json()
            filtered_data = data["results"]
            for item in filtered_data:
                data_list.append(item[f'{property}'])
    return data_list

database = {}
database['starships'] = API_scrape('starships', 'model')
database['planets'] = API_scrape('planets', 'name')
database['species'] = API_scrape('species', 'name')

file = 'sw_database.json'
with open(file, 'w') as f:
    json.dump(database, f)
