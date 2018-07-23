from pytest import raises
from longest_palindromic_substring import longest_palindrome as lp


def test_invalid_param():
    """
    Non-string raises.
    """
    with raises:
        assert lp(7)


def test_empty_string():
    """
    Empty string has no palindromes.
    """
    assert lp('') == []


def test_single_letter():
    """
    Single letter is palindrome.
    """
    assert lp('a') == ['a']


def test_even_simple_palindromes():
    """
    Basic even-lettered palindromes are found.
    """
    assert lp('aa') == ['aa']
    assert lp('abba') == ['abba']


def test_odd_simple_palindromes():
    """
    Basic odd-lettered palindromes are found.
    """
    assert lp('aaa') == ['aaa']
    assert lp('aba') == ['aba']
    assert lp('abcba') == ['abcba']


def test_front_palindrome():
    """
    Longest palindrome at beginning of string.
    """
    assert lp('abaonly') == ['aba']
    assert lp('abbaonly') == ['abba']


def test_rear_palindrome():
    """
    Longest palindrome is at back of string.
    """
    assert lp('onlyaba') == ['aba']
    assert lp('onlyabba') == ['abba']


def test_multiple_identical_palindromes():
    """
    Identical palindromes are only added once.
    """
    assert lp('abadfaba') == ['aba']
    assert lp('abbadfabba') == ['abba']


def test_multiple_palindromes_one_longer():
    """
    Longest palindrome is chosen.
    """
    assert lp('mmaaa') == ['aaa']
    assert lp('mmmaaaa') == ['aaaa']


def test_multiple_palindromes_equal_length():
    """
    Different palindromes of equal length are both added.
    """
    assert sorted(lp('ma')) == ['a', 'm']
    assert sorted(lp('mmaa')) == ['aa', 'mm']
    assert sorted(lp('mmaamm')) == ['aa', 'mm']


def test_middle_palindromes():
    """
    Palindromes in middle of string.
    """
    assert sorted(lp('abcdedcfghijihklm')) == ['cdedc', 'hijih']
