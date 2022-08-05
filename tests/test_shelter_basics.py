import pytest
from animalshelter  import AnimalShelter

# ----- These steps are supposed to run in pytest only

def test_shelter_accepts_animals_until_full():
    shelter = AnimalShelter(5, ('bird',))

    for bird_nr in range(5): 
        shelter.shelter({'Species':'bird',
                        'Name':f'Tweety {bird_nr}',
                        'Age':2})

    try: 
        shelter.shelter({'Species':'bird',
                        'Name':f'Tweety X',
                        'Age':2})
    except Exception:
        # Expecting error because shelter is full
        return True

    assert False, 'Shelter accepted an animal despite it was full'

