Feature: Sheltering of abandoned animals

    Scenario: A shelter without space cannot shelter animals
        Given there is a dog shelter with no space
        Then I cannot shelter a dog

    Scenario: A shelter for cats does not accept birds
        Given a shelter has room for 5 cats
        Then I can shelter a cat
        But I cannot shelter a bird

    Scenario: A shelter for cats and dogs accepts only those species
        Given there is a shelter for 10 animals of species cat or dog
        Then I can shelter a cat
        And I can shelter a dog
        But I cannot shelter a bird

    Scenario: A shelter accepts no more animals than it can handle
        Given there is a shelter for 2 animals of species cat or dog
        And I shelter a cat
        And I shelter a dog
        Then I cannot shelter a cat
