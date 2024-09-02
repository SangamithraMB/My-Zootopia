import requests

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = "pWpm7irdz1ssNUHXgtKTfgzmAxSGG16oWaPI2MDL"


def fetch_animal_data(animal_name):
    """Fetches animal data from the API by name."""
    headers = {
        'X-Api-Key': API_KEY
    }
    params = {
        'name': animal_name
    }

    print(f"Requesting URL: {API_URL} with params: {params}")

    response = requests.get(API_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        print("API Response:", data)
        return data
    else:
        raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")


def serialize_animal(animal_obj):
    """
    Single animal serialization.
    """
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '<div class="cards__text">\n'
    output += '<ul>\n'
    if 'taxonomy' in animal_obj:
        if 'phylum' in animal_obj['taxonomy']:
            output += f'<li><strong>Phylum:</strong> {animal_obj["taxonomy"]["phylum"]}</li>\n'
        if 'scientific_name' in animal_obj['taxonomy']:
            output += f'<li><strong>Scientific Name:</strong> {animal_obj["taxonomy"]["scientific_name"]}</li>\n'
    if 'characteristics' in animal_obj:
        if 'diet' in animal_obj['characteristics']:
            output += f'<li><strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}</li>\n'
        if 'color' in animal_obj['characteristics']:
            output += f'<li><strong>Color:</strong> {animal_obj["characteristics"]["color"]}</li>\n'
        if 'skin_type' in animal_obj['characteristics']:
            output += f'<li><strong>Skin Type:</strong> {animal_obj["characteristics"]["skin_type"]}</li>\n'
        if 'top_speed' in animal_obj['characteristics']:
            output += f'<li><strong>Top Speed:</strong> {animal_obj["characteristics"]["top_speed"]}</li>\n'
        if 'type' in animal_obj['characteristics']:
            output += f'<li><strong>Type:</strong> {animal_obj["characteristics"]["type"]}</li>\n'
    if 'locations' in animal_obj and len(animal_obj['locations']) > 0:
        output += f'<li><strong>Location:</strong> {animal_obj["locations"][0]}</li>\n'
    output += '</ul>\n'
    output += "</div>\n"
    output += "</li>\n"
    print(output)
    return output


def get_unique_skin_types(animals_data):
    """Extract unique skin_type values from animals data."""
    skin_types = set()
    for animal in animals_data:
        if 'characteristics' in animal and 'skin_type' in animal['characteristics']:
            skin_types.add(animal['characteristics']['skin_type'])
    return skin_types


def replace_animal_info(animal_name):
    """
    Replace the HTML template __REPLACE_ANIMALS_INFO__ with the result from the animal data fetched from the API.
    """
    animals_data = fetch_animal_data(animal_name)

    if not isinstance(animals_data, list):
        raise Exception("Unexpected API response format: Expected a list of animals.")

    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    content_to_be_replaced = "__REPLACE_ANIMALS_INFO__"
    with open("animals_template.html", "r", encoding='utf-8') as filehandle:
        template_content = filehandle.read()
    modified_content = template_content.replace(content_to_be_replaced, output)
    with open("animals.html", "w", encoding='utf-8') as fileobject:
        fileobject.write(modified_content)


def main():
    """
    Main Function
    """
    animal_name = input("Enter the name of an animal: ")
    if not animal_name.strip():
        print("Animal name cannot be empty.")
        return
    replace_animal_info(animal_name)
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
