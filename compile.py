#!/usr/bin/python3

import json
import sys
import os
import glob
import configparser
import importlib

def file_contents(*filename):
    with open(os.path.join(directory, *filename)) as f:
        return f.read()

try:
    directory = sys.argv[1]
except IndexError:
    print("Usage: compile.py <directory>")
    sys.exit(1)

chapter = {}
chapter["introduction"] = file_contents("introduction")
chapter["conclusion"] = file_contents("conclusion")
scenes = []
for scene in os.listdir(os.path.join(directory, "scenes")):
    scenes.append(file_contents("scenes", scene))
chapter["scenes"] = scenes

chapter.update(eval(file_contents("vars.py")))

print(json.dumps(chapter))
