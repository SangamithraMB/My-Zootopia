import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = 'https://api.api-ninjas.com/v1/animals'


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.

    Args:
    animal_name (str): The name of the animal to fetch data for.

    Returns:
    list: A list of animals, where each animal is a dictionary with keys like 'name', 'taxonomy', 'locations', and 'characteristics'.
    """
    headers = {'X-Api-Key': API_KEY}
    params = {'name': animal_name}
    response = requests.get(API_URL, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")
