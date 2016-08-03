#!/usr/bin/python3

"""
Story generator based on JSON chapter files.
See README.md for file format.

(c) 2016 Finn Rose Ellis. Licensed under the MIT License.
See LICENSE.txt for license details.
"""

import random
import json
import sys


# Grab the filename from the command line and open it.
if len(sys.argv) == 2:
    chapterfile = sys.argv[1]
else:
    print("Please pass exactly one argument: a chapter filename.")
    sys.exit(1)
with open(chapterfile) as f:
    chapter = json.loads(f.read())


# Reorder the scene list randomly.
random.shuffle(chapter["scenes"])


# Generate and print the story.
if chapter["introduction"]:
    print(chapter["introduction"])

for story in chapter["story"]:
    rejects = []
    found_scene = False
    while chapter["scenes"] and not found_scene:
        try:
            scene = chapter["scenes"].pop()
            print(scene.format(**story))
            # If the print worked, we had the right variables available. 
            found_scene = True
            break
        except KeyError:
            # Didn't have the right variables.
            # Set that scene aside and keep looking.
            rejects.append(scene)
    # Put the rejected scenes for this story piece back.
    chapter["scenes"].extend(rejects)
    if not found_scene:
        print("Couldn't find an appropriate scene for story with these keys:", ", ".join(story.keys()))
        sys.exit(2)

if chapter["conclusion"]:
    print(chapter["conclusion"])
