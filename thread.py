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

import character


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

# Generate character objects.
characters = []
for c in chapter.get("characters", []):
    characters.append(character.Character(c["name"], c["pronouns"]))

# Generate and print the story.
if chapter["introduction"]:
    print(chapter["introduction"])

for story in chapter["story"]:
    # Replace integer variables with the corresponding characters.
    for k,v in story.items():
        try:
            story[k] = characters[v]
        except TypeError:
            # Value wasn't an integer, ignore it.
            pass

    rejects = []
    found_scene = False
    while chapter["scenes"] and not found_scene:
        # Look for a scene whose variables match the next story piece.
        try:
            scene = chapter["scenes"].pop()
            print(scene.format(**story))
            # If the print worked, we had the right variables available. 
            found_scene = True
            break
        except KeyError:
            # Didn't have the right variables, set it aside and keep looking.
            rejects.append(scene)
    # Put the rejected scenes for this story piece back.
    chapter["scenes"].extend(rejects)
    if not found_scene:
        print("Couldn't find an appropriate scene for story with these keys:", ", ".join(story.keys()))
        sys.exit(2)

if chapter["conclusion"]:
    print(chapter["conclusion"])
