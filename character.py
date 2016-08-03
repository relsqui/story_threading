#!/usr/bin/python3

pronouns = {}
pronouns["PINDEX"] = {"they":0, "them":1, "their":2, "theirs":3, "themselves":4}
pronouns["THEY"] = ["they", "them", "their", "theirs", "themselves"]
pronouns["SHE"] = ["she", "her", "her", "hers", "herself"]
pronouns["HE"] = ["he", "him", "his", "his", "himself"]

class Character(object):
    def __init__(self, name="Someone", pron="they"):
        self.name = name
        self.pronouns = pronouns[pron.upper()]
        for k,v in pronouns["PINDEX"].items():
            self.__setattr__(k, self.pronouns[v])
            self.__setattr__(k.title(), self.pronouns[v].title())
            self.__setattr__(k.upper(), self.pronouns[v].upper())

    def __str__(self):
        return self.name

if __name__ == "__main__":

    people = {}
    people["finn"] = Character("Finn")
    people["erik"] = Character("Erik", "he")
    people["ada"] = Character("Ada", "she")

    example = """{finn} is testing {finn.their} code.
{erik} is helping! {erik.They} and {finn} use different pronouns.
So {finn} can write {erik.theirs} next to {finn.theirs} and it should come out different.
This is easier than just testing by {finn.themselves}.
{ada} asked {finn} for all caps so {ada.they} could shout, but {finn.they} will implement it later."""

    print(example.format(**people))
