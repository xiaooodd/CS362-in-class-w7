import pytest
import wordcount

def test1():
    result = wordcount.w_count(" a ")
    assert result == 1

def test2():
    result = wordcount.w_count("Hello world!")
    assert result == 2

def test3():
    result = wordcount.w_count("a++++ b c")
    assert result == 3