
    Install pytest from Terminal - pip install -U pytest
    Change your test file names from *_tests.py to *_test.py
    Replace the import at the beginning of the test from nose to pytest with an import pytest
    Replace your assert_equal() statements to assert ’ == ’ NOTE: Drop the brackets
    E.g. assert_equal(center.go('north') , north) turns into assert center.go('north') == north
    Run your tests from the project directory (one level above the test folder) using the command ‘$pytest’ instead of the command ‘$nosetests’

import pytest
from ex48 import lexicon

def test_directions():
    assert lexicon.scan("north") == [('direction', 'north')]
    result = lexicon.scan("north south east")
    assert result == [
        ('direction', 'north'),
        ('direction', 'south'),
        ('direction', 'east')
    ]



