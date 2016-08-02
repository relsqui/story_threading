#!/usr/bin/python

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

print chapter["introduction"]
print
for i in range(len(chapter["story"])):
    print chapter["scenes"][0].format(**chapter["story"][i])
    print
print chapter["conclusion"]
