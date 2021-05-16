import pytest
import wordcount

def test1(self):
    result = wordcount.w_count(" a ")
    assert result == 1

def test2(self):
    result = wordcount.w_count("Hello world!")
    assert result == 2

def test3(self):
    result = wordcount.w_count("a++++ b c")
    assert result == 3