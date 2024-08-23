import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def convert_to_animals_data(json_content):
    """
    Extracting animal details from the given json content.
    """
    output = ''
    for animal in json_content:
        output += '<li class="cards__item">'
        if 'name' in animal:
            output += f'<div class="card__title">{animal['name']}</div>'
            output += '<p class="cards__text">'
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output += f'<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n'
            output += "<br/>"
        if 'locations' in animal and len(animal['locations']) > 0:
            output += f'<strong>Location:</strong> {animal['locations'][0]}<br/>\n'
            output += "<br/>"
        if 'characteristics' in animal and 'type' in animal['characteristics']:
            output += f'<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n'
        output += "</p>"
        output += "</li>"
    return output


def replace_animal_info():
    """
     Replace the HTML template __REPLACE_ANIMALS_INFO__ with the result from animals data.
    """
    animals_data = load_data('animals_data.json')
    actual_animal_data = convert_to_animals_data(animals_data)
    content_to_be_replaced = "__REPLACE_ANIMALS_INFO__"
    with open("animals_template.html", "r") as filehandle:
        template_content = filehandle.read()
    modified_content = template_content.replace(content_to_be_replaced, actual_animal_data)
    with open("animals.html", "w") as fileobject:
        fileobject.write(modified_content)


def main():
    """
    Main Function
    """
    replace_animal_info()


if __name__ == "__main__":
    main()
