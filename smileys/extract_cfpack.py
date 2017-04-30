import json
import re
import json
__author__ = 'bomzhe'
# cfpack stealer cfpack_st101.zip
# http://alexforum.ws/showthread.php?t=3911&page=3
import struct
import os
import sys
from time import strftime
import base64

ext = {
	b'\x47\x49': 'gif',
	b'\xff\xd8': 'jpg',
	b'\x89\x50': 'png',
	b'\x42\x4d': 'bmp'
}

file_names_pattern = {
	"I" : "base",
	"II" : "girls",
	"III": "extra"
}
smiley_pattern = re.compile(r'^:.*:$')


def extract_file(pack_path, gif_dir_path):
	with open(pack_path, 'rb') as f:
		addition_info, cats = {}, []
		smileys = {}
		start_char = 13313
		b64_data = {}
		print(strftime('[%H:%M:%S] Please wait.'))
		size = struct.unpack('<H', f.read(2))  # header size (useless)
		addition_info['width'], addition_info['height'], count = struct.unpack('<HHB', f.read(5))
		for c in range(count):
			size = ord(f.read(1)) * 2  # 2 байта на символ utf16
			cats.append((f.read(size)).decode('utf-16le'))  # запоминаем категории
			addition_info[cats[c]] = []
			cat_path = os.sep.join((gif_dir_path, file_names_pattern[cats[c]]))
			if not os.path.exists(cat_path):
				os.mkdir(cat_path)
		addition_info['count'] = struct.unpack('<H', f.read(2))[0]  # число смайлов в паке
		for item in range(addition_info['count']):
			f.seek(1, 1)  # размер заголовка пропускаем
			cat_cur = ord(f.read(1))
			if cat_cur >= count:
				raise SyntaxError('File is not valid')
			size = ord(f.read(1)) * 2
			alias = (f.read(size)).decode('utf-16le')
			f.seek(1, 1)  # 0
			size = struct.unpack('<I', f.read(4))[0]
			data = f.read(size)
			file_ext = ext.get(data[:2], '')
			file_name = '{0:04x}.{1}'.format(item, file_ext)
			tab = file_names_pattern[cats[cat_cur]]
			gif_file_path = os.sep.join((gif_dir_path, tab, file_name))
			smileys.setdefault(tab, {})
			if not smiley_pattern.match(alias):
				alias = ":%s:" % alias
			start_char += 1
			smileys[tab][chr(start_char)] = alias
			b64_data[alias] = base64.b64encode(data).decode('utf8')
			with open(gif_file_path, 'wb') as gif:
				gif.write(data)
	return smileys, b64_data



def create_json_info(info, gif_dir_path):
	if not os.path.exists(gif_dir_path):
		os.mkdir(gif_dir_path)
	info_file_name = os.sep.join((gif_dir_path, 'info.json'))
	with open(info_file_name, 'w', encoding='utf-8') as f:
		f.write(json.dumps(info))

def create_sass_file(info, sass_out_path):
	info_file_name = os.sep.join((sass_out_path, '_smileys.sass'))
	with open(info_file_name, 'w', encoding='utf-8') as f:
		f.write('''@import "./mixins"\n''')
		for key in info:
			f.write('''@include smile("{}", "{}")\n'''.format(key, info[key]))


if __name__ == '__main__':
	print('\nCFPack Stealer 1.01\n')
	pack_path = os.sep.join((os.path.dirname(os.path.realpath(__file__)), "DefaultSmilies.cfpack"))
	gif_dir_path = os.sep.join((os.path.dirname(os.path.dirname(__file__)), "smileys"))
	sass_out_path = os.sep.join((os.path.dirname(os.path.dirname(__file__)), "static", "sass", "partials"))
	if not os.path.exists(pack_path):
		raise FileNotFoundError("cfpack file <<%s>> doesn't exist" % pack_path)
	info, b64 = extract_file(pack_path, gif_dir_path)
	create_json_info(info, gif_dir_path)
	create_sass_file(b64, sass_out_path)
	print(strftime('[%H:%M:%S] Done.'))
