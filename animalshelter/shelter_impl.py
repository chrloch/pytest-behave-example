from tkinter import SEL_FIRST
from typing import Iterable, Mapping


class AnimalShelter: 

    def __init__(self, capacity:int, allowed_species:Iterable):
        self._capacity = int(capacity)
        self._allowed_species = set(allowed_species)
        self._animals = []

    def shelter(self, animal:Mapping[str,object]):
        'Provice shelter to an animal'

        assert 'Species' in animal, 'Cannot determine species of furball'
        assert animal.get('Species') in self._allowed_species, \
            f"We don't have the facilities to shelter a {animal.get('Species')}"
        
        assert len(self._animals) < self._capacity, 'We are full. Please adopt a furball'
        self._animals.append(animal)


    def can_adopt( self, species:str ):
        'Checks if an animal of species can be adopted'
        for animal in self._animals:
            if animal['Species'].lower() == species.lower():
                return True
        return False

    def adopt(self, species:str ): 
        '''Adopts an animal of the given species or any species if None is given
            as the species parameter. If adoption was not successful, return None'''
        for animal in self._animals:
            if species is None or animal['Species'].lower() == species.lower():
                self._animals.remove(animal)
                return animal
        
        return None

    @property
    def animals(self):
        return tuple(self._animals)

    @property
    def places_left(self):
        return self._capacity - len(self._animals)
    
