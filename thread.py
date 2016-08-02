#!/usr/bin/python

import random
import json

with open("chapter.json") as f:
    chapter = json.loads(f.read())

random.shuffle(chapter["scenes"])

print chapter["introduction"]
print
for i in range(len(chapter["story"])):
    scene = chapter["scenes"][i]
    story = chapter["story"][i]
    story["var"]["story"] = story["text"]
    print scene.format(**story["var"])
    print
print chapter["conclusion"]
