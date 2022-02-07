import sh
import pytest

def test_sort():
    assert sh.sort("lines") == "1\n2\n2\n2\n23\n45\n45\n54\n65\n67\n8\n9\n"
    
def test_sort_unique():
    assert sh.sort("lines", "-u") == "1\n2\n23\n45\n54\n65\n67\n8\n9\n"

def test_sort_numerically():
    assert sh.sort("lines", "-n") == "1\n2\n2\n2\n8\n9\n23\n45\n45\n54\n65\n67\n"
    
def test_sort_reverse():
    assert sh.sort("lines", "-r") == "9\n8\n67\n65\n54\n45\n45\n23\n2\n2\n2\n1\n"
    
def test_sort_reverse_numerically_unique():
    assert sh.sort("lines", "-run") == "67\n65\n54\n45\n23\n9\n8\n2\n1\n"
