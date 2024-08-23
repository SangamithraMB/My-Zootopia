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
        if 'name' in animal:
            output += f"Name: {animal['name']}\n"
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output += f"Diet: {animal['characteristics']['diet']}\n"
        if 'locations' in animal and len(animal['locations']) > 0:
            output += f"Location: {animal['locations'][0]}\n"
        if 'characteristics' in animal and 'type' in animal['characteristics']:
            output += f"Type: {animal['characteristics']['type']}\n"
        output += "\n"
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
