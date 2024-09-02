import data_fetcher


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


def replace_animal_info(animal_name):
    """
    Replaces the HTML template __REPLACE_ANIMALS_INFO__ with the result from the animal data fetched from the API.

    Args:
    animal_name (str): The name of the animal to fetch data for.
    """
    try:
        animals_data = data_fetcher.fetch_data(animal_name)

        if not animals_data:
            output = f'<h2>No such animal found: "{animal_name}".</h2>'
        else:
            output = ''
            for animal_obj in animals_data:
                output += serialize_animal(animal_obj)

        content_to_be_replaced = "__REPLACE_ANIMALS_INFO__"
        with open("animals_template.html", "r", encoding='utf-8') as filehandle:
            template_content = filehandle.read()
        modified_content = template_content.replace(content_to_be_replaced, output)
        with open("animals.html", "w", encoding='utf-8') as fileobject:
            fileobject.write(modified_content)

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main Function
    """
    animal_name = input("Enter the name of an animal: ")
    replace_animal_info(animal_name)
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
