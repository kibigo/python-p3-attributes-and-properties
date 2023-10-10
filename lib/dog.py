#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    
    def __init__(self, name = "", breed = "Mutt"):
        self._name = ""
        self._breed = ""
        self.name = name
        self.breed = breed


    def name (self):
        return self._name

    def name (self, value):

        if type(value) == str and 1 <= len(value) <= 25:
            self._name = value

        elif value == "":
            return("Name must be string between 1 and 25 characters.")
        
        else:
            return("Name must be string between 1 and 25 characters.")

    def breed(self):
        return self._breed

    def breed(self, value):

        if value in APPROVED_BREEDS:
            self._breed = value

        else:
            print("Breed must be in list of approved breeds.")



