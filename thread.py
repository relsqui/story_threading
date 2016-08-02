#!/usr/bin/python

import random
import json

with open("chapter.json") as f:
    chapter = json.loads(f.read())

random.shuffle(chapter["scenes"])

print chapter["introduction"]
print
for i in range(len(chapter["story"])):
    print chapter["scenes"][0].format(**chapter["story"][i])
    print
print chapter["conclusion"]
