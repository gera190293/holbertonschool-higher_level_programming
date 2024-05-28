#!/usr/bin/python3

import os
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


f = add_item.json
if os.path.exists(f):
    l = load_from_json_file(f)
else:
    l = []
l.extend(sys.argv[1:])
save_to_json_file(l, f)