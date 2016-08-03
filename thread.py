#!/usr/bin/python

"""
Story generator based on JSON chapter files.
See README.md for file format.

(c) 2016 Finn Rose Ellis. Licensed under the MIT License.
See LICENSE.txt for license details.
"""

import random
import json
import sys

if len(sys.argv) == 2:
    chapterfile = sys.argv[1]
else:
    print "Please pass exactly one argument: a chapter filename."
    sys.exit(1)

with open(chapterfile) as f:
    chapter = json.loads(f.read())

random.shuffle(chapter["scenes"])

if chapter["introduction"]:
    print chapter["introduction"]

for story in chapter["story"]:
    rejects = []
    found_scene = False
    while chapter["scenes"] and not found_scene:
        try:
            scene = chapter["scenes"].pop()
            print scene.format(**story)
            found_scene = True
            break
        except KeyError:
            rejects.append(scene)
    chapter["scenes"].extend(rejects)
    if not found_scene:
        print "Couldn't find an approprate scene for story with these keys:", ", ".join(story.keys())
        sys.exit(2)

if chapter["conclusion"]:
    print chapter["conclusion"]
