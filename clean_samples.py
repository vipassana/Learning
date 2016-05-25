import pandas as pd
import json
import re
import glob

real_dict = {}

for filename in glob.glob('*.json'):
	with open(filename) as f:
		all_dicts = f.readlines()
	all_dicts = re.split(r'{*}',all_dicts[0])
	for i in range(len(all_dicts)):
		all_dicts[i] = all_dicts[i][1:]+'}'
		key_date_match = re.findall(r'"([^"]*)"',all_dicts[i])
		follows_match = re.findall(r':(.*)\}', all_dicts[i])
		if key_date_match:
			if follows_match:
				follows_match[0] = re.sub(', "' + re.findall(r'"(.*)\]', follows_match[0])[0], '', follows_match[0])
				follows_match[0] = re.sub('\[\[','[',follows_match[0])
				follows_match[0] = re.sub('\]\]',']',follows_match[0])
				follows_match[0] = follows_match[0].strip()
				follows_match[0] = follows_match[0].strip('[')
				follows_match[0] = follows_match[0].strip(']')
				follows_match = follows_match[0].split(',')

				#follows_match = follows_match[0].split(',')
				for i in range(len(follows_match)):
					follows_match[i] = follows_match[i].strip()
				#for i in range(len(follows_match)):
				#	if follows_match[i] != '':
				#		follows_match[i] = int(follows_match[i])
				#follows_match = map(int, follows_match)
				#follows_match[-1] = int(follows_match[-1])
				real_dict[key_date_match[0]] = [follows_match,key_date_match[1]]

#	for val in all_dicts:
		#print all_dicts[0]
print real_dict.keys()
with open('./result/sampleset.json', 'w') as f:
	json.dump(real_dict,f)
