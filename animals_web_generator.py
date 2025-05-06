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
    name = animal_obj.get("name", "Unbekannt")
    locations = animal_obj.get("locations", [])
    characteristics = animal_obj.get("characteristics", {})

    fields = {
        "🎨 Color": characteristics.get("color"),
        "✨ Most distinctive": characteristics.get("most_distinctive_feature"),
        "📍 Location": locations[0] if locations else None,
        "🛖 Habitat": characteristics.get("habitat"),
        "🏹 Prey": characteristics.get("prey"),
        "🥷 Predators": characteristics.get("predators"),
        "⚖️ Weight": characteristics.get("weight"),
        "📏 Length": characteristics.get("length"),
        "💨 Pace": characteristics.get("top_speed"),
        "⏳ Lifespan": characteristics.get("lifespan"),
    }

    output = ''
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <div class="card__text">\n'
    output += '    <ul class="info-list">\n'

    for label, value in fields.items():
        if value:
            output += f'      <li><strong>{label}:</strong> {value}</li>\n'

    output += '    </ul>\n'
    output += '  </div>\n'
    output += '</li>\n'

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
        "Color": characteristics.get("color"),
        "Signature": characteristics.get("most_distinctive_feature"),
        "Location": locations[0] if locations else None,
        "Habitat": characteristics.get("habitat"),
        "Prey": characteristics.get("prey"),
        "Predators": characteristics.get("predators"),
        "Weight": characteristics.get("weight"),
        "Length": characteristics.get("length"),
        "top_speed": characteristics.get("top_speed"),
        "Lifespan": characteristics.get("lifespan"),

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

