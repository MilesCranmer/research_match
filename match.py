#!/usr/bin/python

import sys, os
import ads as ads

names_file = open(sys.argv[1])

#Default abstract storage
abstract_directory = "abstracts"
if len(sys.argv) > 2:
	abstract_directory = sys.argv[2]

if not os.path.exists(abstract_directory):
	os.makedirs(abstract_directory)

number_abstracts = 4
if len(sys.argv) > 3:
	number_abstracts = int(sys.argv[3])


i = 0
for line in names_file:
	#Only names
	if line[0]==',': continue
	if len(line) < 4: continue

	cut_point = 0

	#Find last space
	for x in reversed(range(len(line))):
		if line[x] == ' ':
			cut_point = x
			break
	first_name = line[:x]
	last_name = line[x+1:]
	last_name = ''.join([char for char in last_name if char.isalpha()])
	papers = ads.SearchQuery(
		author=last_name+", "+first_name,
		sort='date',
		fl=['abstract'])

	abstract_file = open(abstract_directory+"/"+\
		last_name+"_"+first_name+".txt",'w')
	j = 0
	for paper in papers:
		abstract_file.write("Abstract "+str(j)+"\n")
		try:
			abstract_file.write(paper.abstract.encode('utf-8'))
		except AttributeError:
			pass
		abstract_file.write("\n")
		j += 1
		if j > number_abstracts: break
	i+=1
	if i > 4:
		break
	print i
