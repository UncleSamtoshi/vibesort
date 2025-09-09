from vibesort import vibesort, vibeequals
from dotenv import load_dotenv

load_dotenv()


def test_vibesort():
    assert vibesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert vibesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert vibesort([1, 3, 2, 5, 4]) == [1, 2, 3, 4, 5]


def test_long_array():
    assert vibesort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert vibesort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert vibesort([1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_vibeequals_identical_values():
    """Test that identical values are considered equal"""
    assert vibeequals("hello", "hello") == True
    assert vibeequals(42, 42) == True
    assert vibeequals([1, 2, 3], [1, 2, 3]) == True


def test_vibeequals_different_formats():
    """Test that semantically equal but differently formatted values are considered equal"""
    assert vibeequals("Hello", "hello") == True  # case difference
    assert vibeequals("42", 42) == True  # string vs number
    assert vibeequals("yes", "true") == True  # synonymous values


def test_vibeequals_different_values():
    """Test that truly different values are not considered equal"""
    assert vibeequals("hello", "goodbye") == False
    assert vibeequals(42, 7) == False
    assert vibeequals("yes", "no") == False
