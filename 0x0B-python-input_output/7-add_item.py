#!/usr/bin/python3
"""a script that adds all arguments to a Python list
    and then save them to a file"""


import sys
from os.path import exists
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
if exists(filename):
    mytxt = load_from_json_file(filename)
else:
    mytxt = []
mytxt.extend(sys.argv[1:])
save_to_json_file(mytxt, filename)
