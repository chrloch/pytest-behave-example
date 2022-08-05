from behave import *
from animalshelter import AnimalShelter
from random import randint
import pytest

# ----- These steps are supposed to run in behave AND in pytest


@given('there is a dog shelter with no space')
def test_there_is_a_shelter_with_no_space(context):
    context.shelter = AnimalShelter(capacity=0, allowed_species=('dog',))


@then('I cannot shelter a {species}')
@pytest.mark.parametrize('species', ('cat', 'dog', 'mouse'))
def test_cannot_shelter_a(context, species):
    try:
        test_shelter_a(context, species)
    except AssertionError:
        return True
    assert False, f'Should not be able to shelter a {species}'


@given('a shelter has room for {capacity} cats')
@pytest.mark.parametrize('capacity', (10,))
def test_create_shelter_for_cats(context, capacity):
    context.shelter = AnimalShelter(
        capacity=int(capacity), allowed_species=('cat',))


@given('I shelter a {species}')
@then('I can shelter a {species}')
@pytest.mark.parametrize('species', ('cat',))
def test_shelter_a(context, species):
    context.shelter.shelter({'Species': species,
                             'Name': f'Furball {randint(1,1000)}',
                             'Age': randint(1, 10)})


# ----- These steps are supposed to run in behave only

@given('there is a shelter for {capacity} animals of species {species1} or {species2}')
def there_is_a_shelter_for_2_species(context, capacity, species1, species2):
    context.shelter = AnimalShelter(capacity=int(
        capacity), allowed_species=(species1, species2))
