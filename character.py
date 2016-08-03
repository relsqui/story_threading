#!/usr/bin/python3

THEY = ["they", "them", "their", "theirs", "themselves"]
PKEY = {"they":0, "them":1, "their":2, "theirs":3, "themselves":4}
SHE = ["she", "her", "her", "hers", "herself"]
HE = ["he", "him", "his", "his", "himself"]

class Character(object):
    def __init__(self, name="Someone", pronouns=THEY):
        self.name = name
        self.pronouns = pronouns
        for k,v in PKEY.items():
            self.__setattr__(k, pronouns[v])
            self.__setattr__(k.title(), pronouns[v].title())
            self.__setattr__(k.upper(), pronouns[v].upper())

    def __str__(self):
        return self.name

if __name__ == "__main__":

    people = {}
    people["finn"] = Character("Finn")
    people["erik"] = Character("Erik", HE)
    people["ada"] = Character("Ada", SHE)

    example = """{finn} is testing {finn.their} code.
{erik} is helping! {erik.They} and {finn} use different pronouns.
So {finn} can write {erik.theirs} next to {finn.theirs} and it should come out different.
This is easier than just testing by {finn.themselves}.
{ada} asked {finn} for all caps so {ada.they} could shout, but {finn.they} will implement it later."""

    print(example.format(**people))
