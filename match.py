#!/usr/bin/python
#Basically a grep on the abstract directory
import os, sys
import re

#Default abstract storage
abstract_directory = sys.argv[1]

#All search keywords (these can be regex!)
keywords = list(sys.argv[2:])

for dirname, subdirlist, filelist in os.walk(abstract_directory):
	for fname in filelist:
		abs_file = open(abstract_directory+"/"+\
				fname, 'r')
		abs_text = abs_file.read()
		for key in keywords:
			if not re.search(key, 
				abs_text,
				re.IGNORECASE):
				break
		else:
			print fname[:-4]
