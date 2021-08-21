import json

with open('data_lists.json', 'r') as read_file:
    data = json.load(read_file)

print(data)