import json
from pprint import pprint

with open('gif_base64.json') as bash_file:
    data_bash = json.load(bash_file)

with open('info.json') as old_file:
    data_old = json.load(old_file)

new_array = {}
start_char = 13313
for base_type in data_bash:
    new_array[base_type] = {}
    new = {v: k for k, v in data_old[base_type].items()}
    for smile_name in data_bash[base_type]:
        start_char += 1
        new_array[base_type][chr(start_char)] = {}
        new_array[base_type][chr(start_char)]['base64'] = data_bash[base_type][smile_name]
        new_array[base_type][chr(start_char)]['text_alt'] = new["{}.gif".format(smile_name)]

with open('smileys_data.json', 'w') as outfile:
    json.dump(new_array, outfile)