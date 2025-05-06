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
    output += f'    <div class="card__title">{name}</div>\n'
    output += '    <div class="card__text">\n'
    output += '      <ul class="card__list">\n'

    characteristics = animal_obj.get('characteristics', {})
    locations = animal_obj.get('locations', [])

    fields = {
        "Diet": characteristics.get("diet"),
        "Location": locations[0] if locations else None,
        "Type": characteristics.get("type"),
        "Lifespan": characteristics.get("lifespan"),
        "Group": characteristics.get("group"),
        "Color": characteristics.get("color"),
        "Skin Type": characteristics.get("skin_type"),
    }

    for label, value in fields.items():
        if value:
            output += f'        <li><strong>{label}:</strong> {value}</li>\n'

    output += '      </ul>\n'
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

