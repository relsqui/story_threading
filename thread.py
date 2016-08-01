#!/usr/bin/python

import random

def filestring(filename):
    with open(filename) as f:
        return f.read()

ordinals = ["first", "second", "third"]
scenes = ["scene-market", "scene-family", "scene-inn"]
stories = ["story1", "story2", "story3"]

# randomize the scene order
random.shuffle(scenes)


print filestring("introduction")
print
for i in range(len(scenes)):
    scene = filestring(scenes[i])
    story = filestring(stories[i])
    print scene.format(ordinal=ordinals[i], story=story)
    print
print filestring("conclusion")
