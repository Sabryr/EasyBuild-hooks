#!/usr/bin/env python
#sabryr 10-06-2021

import sys
from os import path

def post_package_hook(self):
	if len(sys.argv) >1:
		eb_file = sys.argv[1]
		print("Arguments of the script : ", eb_file)	
		if path.exists(eb_file):
			print("File found ", eb_file)
		else:
			print("Not a file ", eb_file)
	else:
		print("no arguments")

def test_print_dbpath():
	print("ToDo, write a test")

if __name__ == "__main__":
	post_package_hook(None)
