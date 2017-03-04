#!/usr/bin/python

import sys, os
import ads
from nameparser import HumanName

reload(sys)
sys.setdefaultencoding('utf8')

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

author_num = 0
for line in names_file:
	#Only names
	if line[0]==',': continue
	if len(line) < 4: continue

	print "Author", author_num

        parsed_name = HumanName(line)
        papers = ads.SearchQuery(
                author=parsed_name.first+", "+parsed_name.last,
                sort='date',
                fl=['abstract'])
	abstract_file = open(abstract_directory+"/"+\
		parsed_name.first+" "+parsed_name.last+".txt",'w')
	j = 0
        try:
            for paper in papers:
                    abstract_file.write("Abstract "+str(j)+"\n")
                    try:
                            abstract_file.write(paper.abstract.encode('utf-8'))
                    except AttributeError:
                            pass
                    abstract_file.write("\n")
                    j += 1
                    if j > number_abstracts: break
        except ads.base.APIResponseError:
            continue
	author_num+=1
