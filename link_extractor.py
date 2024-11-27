import json 

with open('results.json') as input_file:
    links = json.loads(input_file.read())

print(links)