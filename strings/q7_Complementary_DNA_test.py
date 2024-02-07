import string
from hypothesis.strategies import just, text, lists, integers

from hypothesis import given, example, strategies as st

from q7_Complementary_DNA import dna_strand


test_cases = {
    'ATTGC': 'TAACG',
    'GTAT': 'CATA',
    'AAAA': 'TTTT',
}


@given(st.sampled_from(list(test_cases.keys())))
def test_dna_strand_example(word):
    result = dna_strand(word)
    assert result == test_cases[word], f"Incorrect answer for \"{word}\""


@given(st.text(alphabet=string.ascii_letters, min_size=1))
def test_dna_strand_generator(word):
    result = dna_strand(word)
    expected_result = 'dna_strand(word)'
    assert result == expected_result, f"Incorrect answer for \"{word}\""
