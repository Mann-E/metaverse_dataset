import json 

wget_links = []

with open('results.json') as input_file:
    links = json.loads(input_file.read())

for link_list in links:
    for link in link_list:
        wget_links.append(link)

with open('wget_list.txt', 'w') as wget:
    for w in wget_links:
        wget.write(f'{w}\n')

print("Made the list")