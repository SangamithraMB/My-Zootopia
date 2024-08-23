import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


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


def replace_animal_info(filtered_animals):
    """
     Replace the HTML template __REPLACE_ANIMALS_INFO__ with the result from animals data.
    """
    output = ''
    for animals_obj in filtered_animals:
        output += serialize_animal(animals_obj)
    content_to_be_replaced = "__REPLACE_ANIMALS_INFO__"
    with open("animals_template.html", "r") as filehandle:
        template_content = filehandle.read()
    modified_content = template_content.replace(content_to_be_replaced, output)
    with open("animals.html", "w") as fileobject:
        fileobject.write(modified_content)


def main():
    """
    Main Function
    """
    animals_data = load_data('animals_data.json')

    skin_types = get_unique_skin_types(animals_data)
    print("Available skin types:")
    for i, skin_type in enumerate(skin_types, 1):
        print(f"{i}. {skin_type}")

    user_choice = input("Enter the skin type you want to filter by: ").strip()

    filtered_animals = [animal for animal in animals_data if
                        'characteristics' in animal and animal['characteristics'].get('skin_type') == user_choice]

    if not filtered_animals:
        print(f"No animals found with skin type: {user_choice}")

    replace_animal_info(filtered_animals)


if __name__ == "__main__":
    main()
