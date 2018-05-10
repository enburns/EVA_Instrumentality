#!/usr/bin/python2
import re
from pprint import pprint
def open_file(filename):
	try:
		fp = open(filename)
	except IOError as e:
		if e.errno == errno.ENOENT:
			print "Error: Cannot find file {} at src/".format(filename)
			return None
		raise
	else:
		with fp:
			return fp.readlines()
def read_user_info():
	infos = open_file("user_info.config")
	if infos is None:
		return None
	user = dict()
	for line in infos:
		m = re.search(r'(.+)="(.+)"', line)
		if m:
			user[m.group(1)] = m.group(2)
		else:
			print("Error: formatting errors detected. Is your user_info.config correctly formatted?")
			return None
	return user
def main():
	read_user_info()

if __name__ == "__main__":
	main()
