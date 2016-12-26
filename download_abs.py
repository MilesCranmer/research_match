#!/usr/bin/python
start_url="http://adsabs.harvard.edu/cgi-bin/nph-abs_connect?db_key=AST&db_key=PRE&qform=AST&arxiv_sel=astro-ph&arxiv_sel=cond-mat&arxiv_sel=cs&arxiv_sel=gr-qc&arxiv_sel=hep-ex&arxiv_sel=hep-lat&arxiv_sel=hep-ph&arxiv_sel=hep-th&arxiv_sel=math&arxiv_sel=math-ph&arxiv_sel=nlin&arxiv_sel=nucl-ex&arxiv_sel=nucl-th&arxiv_sel=physics&arxiv_sel=quant-ph&arxiv_sel=q-bio&aut_req=YES&aut_logic=OR&obj_logic=OR&author="
end_url="&object=&start_mon=&start_year=&end_mon=&end_year=&ttl_logic=OR&title=&txt_logic=OR&text=&nr_to_return=10&start_nr=1&jou_pick=ALL&ref_stems=&data_and=NO&abstract=YES&group_and=ALL&start_entry_day=&start_entry_mon=&start_entry_year=&end_entry_day=&end_entry_mon=&end_entry_year=&min_score=&sort=NDATE&data_type=PLAINTEXT&aut_syn=YES&ttl_syn=YES&txt_syn=YES&aut_wt=1.0&obj_wt=1.0&ttl_wt=0.3&txt_wt=3.0&aut_wgt=YES&obj_wgt=YES&ttl_wgt=YES&txt_wgt=YES&ttl_sco=YES&txt_sco=YES&version=1"

import sys, os
import urllib2

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

	print first_name+'_'+last_name+'.txt'

	query_name = first_name+'%2C+'+last_name
	query = start_url + query_name + end_url.replace('10', str(number_abstracts))

	print query
	response = urllib2.urlopen(query)
	html = response.read()

		
	participant_file = open(abstract_directory+'/'+\
		first_name+'_'+last_name+'.txt', 'w')

	participant_file.write(html)
	i+=1
	if i >= 2:
		break
