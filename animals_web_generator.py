import json

def load_data(file_path):
    """loads a JSON-file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

data = load_data('animals_data.json')

def get_animals_data():
    """returns a string with the animal"""
    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output

def serialize_animal(animal_obj):
    output = '<li class="cards__item">\n'
    output += '  <div class="card">\n'

    name = animal_obj.get("name", "Unbekannt")
    output += f'    <div class="card__header"><h2 class="card__title">{name}</h2></div>\n'
    output += '    <div class="card__body">\n'

    characteristics = animal_obj.get('characteristics', {})
    diet = characteristics.get('diet')
    if diet:
        output += f'      <p><strong>Diet:</strong> {diet}</p>\n'

    locations = animal_obj.get('locations', [])
    if locations:
        output += f'      <p><strong>Location:</strong> {locations[0]}</p>\n'

    type_ = characteristics.get('type')
    if type_:
        output += f'      <p><strong>Type:</strong> {type_}</p>\n'

    output += '    </div>\n'
    output += '  </div>\n'
    output += '</li>\n'
    return output

animals_data = get_animals_data().strip()

with open('animals_template.html', 'r') as file:
    template = file.read()
    new_html = template.replace('__REPLACE_ANIMALS_INFO__', animals_data)

with open('animals.html', 'w', encoding="utf-8") as file:
    file.write(new_html)

