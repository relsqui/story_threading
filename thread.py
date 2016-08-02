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

print chapter["introduction"]
print
for i in range(len(chapter["story"])):
    print chapter["scenes"][0].format(**chapter["story"][i])
    print
print chapter["conclusion"]
