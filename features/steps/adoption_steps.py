from behave import *

# ----- These steps are supposed to run in behave only

@when('I try to adopt a {species}')
def i_try_to_adopt(context, species):
    context.adopted_animal = context.shelter.adopt(species)


@then('I did not get a new pet')
def i_did_not_get_a_pet(context):
    assert context.adopted_animal is None, 'I should not have gotten a pet'

@then('my new pet is a {species}')
def my_new_pet_is_a(context, species):
    assert context.adopted_animal.get('Species').lower() == species.lower(), \
        f"I expected a {species} but I got {context.adopted_animal}"