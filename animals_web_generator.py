import json

def load_data(file_path):
    """loads a JSON-file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

data = load_data('animals_data.json')

def get_animals_data():
    """returns a string with the animal"""
    output = ''
    for animal in data:
        output += '<li class="cards__item">\n'
        output += f'  <div class="card__title">{animal.get("name", "Unbekannt")}</div>\n'
        output += '  <p class="card__text">\n'

        characteristics = animal.get('characteristics', {})
        diet = characteristics.get('diet')
        if diet:
            output += f'    <strong>Diet:</strong> {diet}<br/>\n'

        locations = animal.get('locations', [])
        if locations:
            output += f'    <strong>Location:</strong> {locations[0]}<br/>\n'

        type_ = characteristics.get('type')
        if type_:
            output += f'    <strong>Type:</strong> {type_}<br/>\n'

        output += '  </p>\n'
        output += '</li>\n'

    return output

animals_data = get_animals_data().strip()

with open('animals_template.html', 'r') as file:
    template = file.read()
    new_html = template.replace('__REPLACE_ANIMALS_INFO__', animals_data)

with open('animals.html', 'w') as file:
    file.write(new_html)

