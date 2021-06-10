#!/usr/bin/env python
#sabryr 10-06-2021

import sys
from os import path
import re
#modloadmsg = "Database location : /cluster/shared"

def post_package_hook(self):
	if len(sys.argv) >1:
		eb_file = sys.argv[1]
		print("Arguments of the script : ", eb_file)	
		if path.exists(eb_file):
			append_info(eb_file)
		else:
			print("Not a file ", eb_file)
	else:
		print("no arguments")

def append_info(filepath):
	content = None
	with open(filepath, "r") as f:
		content = f.readlines()

	#ToDo:Take the last line finding out of this funtion
	r = re.compile(".*moduleclass.*")
	r2 = re.compile(".*Database location.*")
	print(len(content))
	moduleclasses=list(filter(r.match, content))
	if len(moduleclasses)>0:
		module_class_loc=content.index(moduleclasses[-1])
		database_locs=list(filter(r2.match, content))
		print(len(database_locs))
		if len(database_locs)==0:
			print("It seems you are trying to install a module that needs reference data")
			print("We have already setup this data in a central location")
			print("Please include the following line in the easybuild file and then then do the instlation again")

	
def test_print_dbpath():
	print("ToDo, write a test")


if __name__ == "__main__":
	post_package_hook(None)
