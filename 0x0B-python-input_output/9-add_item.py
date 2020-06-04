#!/usr/bin/python3
"""
file: 9-add_item.py
[Script for create JSON]
"""
from os import path
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

file = "add_item.json"

arg = []
if path.isfile(file):
    arg = load_from_json_file(file)

for i in argv[1:]:
    arg.append(i)

save_to_json_file(arg, "add_item.json")
