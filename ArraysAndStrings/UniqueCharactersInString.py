# Chapter 1 - Arrays and Strings
# 1.1
# Implement an algorithm to determine if a string has all unique characters. What if you
# can not use additional data structures?

def is_string_unique(string_to_check):
    """
    Uses a list to check if a string contains unique characters. Can also implement the same using dictionary
    Time Analysis: O(n^2)
    """
    assert isinstance(string_to_check,str), 'Given value is not of type str'

    if string_to_check == "":
        return True

    tracker = []
    for char in string_to_check:
        if char not in tracker:
            tracker.append(char)
        else:
            return False
    return True

def is_string_unique_v2(string_to_check):
    """
    Uses a set to check if a string contains unique characters
    Time Analysis: O(n)
    """
    assert isinstance(string_to_check,str), 'Given value is not of type str'

    if string_to_check == "":
        return True

    #know the difference! set([val]), set(val,), set(val)
    return len(set(string_to_check)) == len(string_to_check)


def is_string_unique_basic(string_to_check):
    """
    No Data structures! Uses bit checks.
    Time: O(n)
    """
    assert isinstance(string_to_check,str), 'Given value is not of type str'

    if string_to_check == "":
        return True

    tracker = 0
    for character in string_to_check:
        ascii_value = ord(character) # can - ord('a') since ascii alphabet a starts at 97
        if tracker & (1 << ascii_value):
            return False
        else:
            tracker |= (1 << ascii_value)
    return True
