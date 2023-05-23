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
    def __init__(self, name = "dog", breed="Pointer"):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        try:
            if(type(name) == str) and (len(name) >= 1) and (len(name) <= 25):
                self._name = name 
            else:
                raise NameError("Name must be string between 1 and 25 characters.")
        except NameError as err:
            print(err)

    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        try:
            if(breed in APPROVED_BREEDS):
                self._breed = breed
            else:
                raise LookupError("Breed must be in list of approved breeds.")
        except LookupError as err:
            print(err)

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)