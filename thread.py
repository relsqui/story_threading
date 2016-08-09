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
import fileinput

import character


# Grab the filename from the command line and open it.
with fileinput.input() as f:
    chapter = json.loads("\n".join(f))

# Reorder the scene list randomly.
random.shuffle(chapter["scenes"])

# Generate character objects.
characters = []
for c in chapter.get("characters", []):
    characters.append(character.Character(c["name"], c["pronouns"]))

# Replace integer globals with the appropriate character.
if "globals" not in chapter:
    chapter["globals"] = {}
for k,v in chapter["globals"].items():
    try:
        chapter["globals"][k] = characters[v]
    except TypeError:
        # Value wasn't an integer, ignore it.
        pass

# Generate and print the story.
if chapter["introduction"]:
    print(chapter["introduction"].format(**chapter["globals"]))

for story in chapter["story"]:
    # Replace integer variables with the corresponding characters.
    for k,v in story.items():
        try:
            story[k] = characters[v]
        except TypeError:
            # Value wasn't an integer, ignore it.
            pass

    # Add globals to the available story variables.
    story.update(chapter["globals"])

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
    print(chapter["conclusion"].format(**chapter["globals"]))
