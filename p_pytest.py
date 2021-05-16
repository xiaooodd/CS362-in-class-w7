import pytest
import palindrome

def test1(self):
    result = palindrome.is_p("a")
    assert result == True

def test2(self):
    result = palindrome.is_p("a++a")
    assert result == True

def test3(self):
    result = palindrome.is_p("a456sd")
    assert result == False