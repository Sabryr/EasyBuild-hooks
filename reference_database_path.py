#!/usr/bin/env python
#sabryr 10-06-2021
#https://github.com/easybuilders/easybuild-framework/blob/develop/easybuild/framework/easyconfig/easyconfig.py
#This is an EasyBuild hook to include database location for relevent modules 
# The hook is trigger when exact match of file in /cluster/shared/databases/module-trigers
# with the eb file name variable is found 

import sys
from os import path
import re
from os import listdir
from os.path import isfile, join

#modloadmsg = "Database location : /cluster/shared"
# MODULES_TO_CHECK=["BLAST+","BLAST", "BUSCO", "Kraken2"]

LOCATION_PREFIX="/cluster/shared/databases/module-trigers/"
#MODULES_TO_CHECK=[]

def get_modules_to_fix():
	MODULES_TO_CHECK = [f for f in listdir(LOCATION_PREFIX) if isfile(join(LOCATION_PREFIX, f))]
	#print(MODULES_TO_CHECK)
	return MODULES_TO_CHECK

def parse_hook2(self):
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
	moduleclasses=list(filter(r.match, content))
	if len(moduleclasses)>0:
		location_to_modify=content.index(moduleclasses[-1])
		database_locs=list(filter(r2.match, content))
		if len(database_locs)==0:
			print("It seems you are trying to install a module that needs reference data")
			print("We have already setup this data in a central location")
			print("Please include the following line in the easybuild file and then then do the instlation again")
			print("Modification needed ")
			print("File to be modify, (please make a copy and modify, keep the original)")
			print("-------------------")
			print(filepath)
			print("-------------------")
			print("Include the following in line ",location_to_modify)

	
def test_print_dbpath():
	print("ToDo, write a test")

def inject_v(eco):
	#eco.log.info("[pre-configure hook] including Database location") 
	#eco.cfg['configopts'] = eco.cfg['configopts'].replace('--with-verbs', '--without-verbs')
	print(type(eco))

def read_info_for_module_name(module_name):
	return read_info(LOCATION_PREFIX+module_name)

def read_info(filepath):
	DB_LOC=""
	print("Database_location filepath = "+filepath)
	with open(filepath, "r") as f:
		while True:
			line = f.readline()
			if line.startswith('Database_location='):
 				#DB_LOC=line.split("=", 1)[1] 
 				DB_LOC=line
				break
	return DB_LOC
	
def parse_hook(self):
	#print(self.name)
	MODULES_TO_CHECK=get_modules_to_fix()
	#print(MODULES_TO_CHECK)
	if self.name in MODULES_TO_CHECK:
		#inject_v(self)
		DB_LOC=read_info(LOCATION_PREFIX+self.name)
		#print("DB_LOC"+DB_LOC)
		self['modloadmsg']=DB_LOC
		#print(self['modloadmsg'])

if __name__ == "__main__":
	#parse_hook(None)
	get_modules_to_fix()

