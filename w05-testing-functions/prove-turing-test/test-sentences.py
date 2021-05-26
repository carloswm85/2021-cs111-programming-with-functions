from sentences import get_determiner, get_noun, get_verb
import pytest


def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["the", "one"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many"]
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    singular_nouns = ["adult", "bird", "boy", "car",
                      "cat", "child", "dog", "girl", "man", "woman"]
    for _ in range(4):
        word = get_noun(1)
        assert word in singular_nouns

    plural_nouns = ["adults", "birds", "boys", "cars",
                    "cats", "children", "dogs", "girls", "men", "women"]
    for _ in range(4):
        word = get_noun(0)
        assert word in plural_nouns


def test_get_verb():
    # Past
    past_tense = ["drank", "ate", "grew", "laughed", "thought",
                  "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        word = get_verb(1, 'past')
        assert word in past_tense

        # Present and singular
    present_tense_singular = ["drinks", "eats", "grows", "laughs",
                              "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        word = get_verb(1, 'present')
        assert word in present_tense_singular

        # Present and Plural
    present_tense_plural = ["drink", "eat", "grow", "laugh",
                            "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        word = get_verb(2, 'present')
        assert word in present_tense_plural

        # Future
    future_tense = ["will drink", "will eat", "will grow", "will laugh",
                    "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(4):
        word = get_verb(1, 'future')
        assert word in future_tense


path = 'E:/GitHub/2021-cs111-programming-with-functions/w05-testing-functions/prove-turing-test/test-sentences.py'
pytest.main(["-v", "--tb=line", "-rN", path])
