Feature: Adoption of sheltered animals 

Scenario: I cannot adopt an animal from an empty shelter
    Given there is a shelter for 10 animals of species cat or dog
     When I try to adopt a dog
     Then I did not get a new pet

Scenario: I can adopt a cat from a shelter that has a cat
    Given there is a shelter for 10 animals of species cat or dog
     And I shelter a cat
     And I shelter a dog
    When I try to adopt a cat
     Then my new pet is a cat
