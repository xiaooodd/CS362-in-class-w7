import pytest
import palindrome

def test1():
    result = palindrome.is_p("a")
    assert result == True

def test2():
    result = palindrome.is_p("a++a")
    assert result == True

def test3():
    result = palindrome.is_p("a456sd")
    assert result == False