import json 

wget_links = []

with open('results.json') as input_file:
    links = json.loads(input_file.read())

for link_list in links:
    for link in link_list:
        print(link)