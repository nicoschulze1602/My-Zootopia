import json
import pprint

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')

for animal in animals_data:
  locations = animal['locations']
  characteristics = animal['characteristics']

  print(f'\nName: {animal['name']}')
  print(f'Diet: {characteristics['diet']}')
  print(f'Location: {locations[0]}')
  try:
      print(f'Type: {characteristics['type']}')
  except KeyError:
      continue



"""pprint.pprint(animals_data[0])
print("- - - - - - - - - - -")
pprint.pprint(animals_data[1]['name'])
print("- - - - - - - - - - -")
pprint.pprint(animals_data[5]['characteristics'])
print("- - - - - - - - - - -")
pprint.pprint(animals_data[10]['locations'])"""
