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


    parsed_name = HumanName(line)
    name_for_ads = parsed_name.last + ', ' + parsed_name.first
    if len(parsed_name.middle) > 0 and len(parsed_name.first) > 2:
        name_for_ads = parsed_name.last + ', ' + parsed_name.first
        name_for_ads += ' ' + parsed_name.middle # ADS bad with two initials
    print "Author:", name_for_ads
    papers = ads.SearchQuery(
            q='author:"'+name_for_ads+'" database:astronomy property:refereed',
            sort='date',
            rows=500,
            fl=['abstract', 'author'])
    abstract_file = open(abstract_directory+"/"+\
        parsed_name.first+"_"+parsed_name.last+".txt",'w')
    j = 0
    while True:
        try:
            for paper in papers:
                try:
                    if len(paper.abstract) < 10:
                        continue
                except TypeError:
                    continue
                if len(paper.author) > 50:
                    continue # Too many authors!
                try:
                    encoded = paper.abstract.encode('utf-8')
                except AttributeError:
                    continue
                abstract_file.write("Abstract "+str(j)+"\n")
                abstract_file.write(encoded)
                abstract_file.write("\n")
                j += 1
                if j > number_abstracts:
                    break
        except ads.base.APIResponseError:
            pass
        else:
            break
    author_num+=1
