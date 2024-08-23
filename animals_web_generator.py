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
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_obj['name']}</div>'
    output += '<p class="cards__text">'
    if 'characteristics' in animal_obj and 'diet' in animal_obj['characteristics']:
        output += f'<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n'
        output += "<br/>"
    if 'locations' in animal_obj and len(animal_obj['locations']) > 0:
        output += f'<strong>Location:</strong> {animal_obj['locations'][0]}<br/>\n'
        output += "<br/>"
    if 'characteristics' in animal_obj and 'type' in animal_obj['characteristics']:
        output += f'<strong>Type:</strong> {animal_obj['characteristics']['type']}<br/>\n'
    output += "</p>\n"
    output += "</li>\n"
    print(output)
    return output


def replace_animal_info():
    """
     Replace the HTML template __REPLACE_ANIMALS_INFO__ with the result from animals data.
    """
    animals_data = load_data('animals_data.json')
    output = ''
    for animals_obj in animals_data:
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
    replace_animal_info()


if __name__ == "__main__":
    main()
