import json
import pprint

def load_data(file_path):
  with open(file_path, "r") as handle:
    return json.load(handle)

data = load_data('animals_data.json')


def print_animals_data(data):
  output = ''
  for animal_data in data:
    output += '\n'

    # Name (nur wenn vorhanden)
    if 'name' in animal_data:
      output += f"Name: {animal_data['name']}\n"

    # Characteristics (nur wenn vorhanden)
    characteristics = animal_data.get('characteristics')
    if characteristics:
      if 'diet' in characteristics:
        output += f"Diet: {characteristics['diet']}\n"
      if 'type' in characteristics:
        output += f"Type: {characteristics['type']}\n"

    # Locations (nur wenn Liste vorhanden & nicht leer)
    locations = animal_data.get('locations')
    if locations and isinstance(locations, list) and len(locations) > 0:
      output += f"Location: {locations[0]}\n"

  return output


#template = load_data('animals_template.html')
print_animals_data()