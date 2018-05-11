#!/usr/bin/python2

#This module defines project, analysis, and file calsses
import os
import os.path
from pprint import pprint
class file:


class analysis:
	def __init__(self, proj, path):
	#a path to the analysis directory is expected
		self.title = None
		self.alias = None
		self.description = None
		self.prj = proj

class project:
	def read_proj_info(path):
		try 

	def __init__(self, path):
	#a path to the project directory is expected
		self.title = None
		self.alias = None
		self.description = None
		self.center = None
		self.taxid = None
		#for each analysis folder, initiate an anlysis instance
		self.analyses = []
		for dir in os.listdir(path):
			if dir == "project_info.config":
				read_proj_info(os.path.join(path,dir))
			else:
				print("No project info file found in {}, be sure you input them manually".format(dir))
			elif os.path.isdir(dir):
				self.analyses.append(analysis(self, os.path.join(path,dir)))
