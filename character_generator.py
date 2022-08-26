import random
import json

WEAPONS = ('lightsaber', 'bowcaster', 'blaster pistol', 'electrostaff', 'flamethrower')

with open('sw_database.json', 'r') as f:
    data = json.load(f)
    
def build_character(database, name):
    """ Return a Star Wars character sheet."""

    species_length = len(database['species']) - 1
    planets_length = len(database['planets']) - 1
    starships_length = len(database['starships']) - 1

    character = f"""
    Name: {name}
    Species: {database['species'][random.randint(0, species_length)]}
    Planet: {database['planets'][random.randint(0, planets_length)]}
    Vehicle: {database['starships'][random.randint(0, starships_length)]}
    Weapon of choice: {WEAPONS[random.randint(0, 4)]}
    """
    
    return character
