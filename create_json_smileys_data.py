import json
from pprint import pprint

with open('gif_base64.json') as bash_file:
    data_bash = json.load(bash_file)

with open('static/smileys/info.json') as old_file:
    data_old = json.load(old_file)

new_array = {}
for base_type in data_bash:
    new_array[base_type] = {}
    new = {v: k for k, v in data_old[base_type].items()}
    for smile_name in data_bash[base_type]:
        new_array[base_type][new["{}.gif".format(smile_name)]] = data_bash[base_type][smile_name]

with open('static/smileys/smileys_data.json', 'w') as outfile:
    json.dump(new_array, outfile)