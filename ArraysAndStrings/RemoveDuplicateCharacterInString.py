# Chapter 1 - Arrays and Strings
# 1.3
# Design an algorithm and write code to remove the duplicate characters in a string
# without using any additional buffer. NOTE: One or two additional variables are fine.
# An extra copy of the array is not.
# FOLLOW UP
# Write the test cases for this method.

"""
Test Cases:
1. String does not contain any duplicates, e.g.: abcd
2. String contains all duplicates, e.g.: aaaa
3. Null string
4. Empty string
5. String with all continuous duplicates, e.g.: aaabbb
6. String with non-contiguous duplicates, e.g.: abababa
"""

def remove_duplicates(string_to_remove):
    if not isinstance(string_to_remove,str):
        return string_to_remove
    elif len(string_to_remove) < 2:
        return string_to_remove
    else:
        if len(set(string_to_remove)) == len(string_to_remove):
            print 'No duplicates'
            return string_to_remove
        else:
            print 'duplicates detected'
            tracker = set()
            for character in string_to_remove:
                if character not in tracker:
                    tracker.add(character)
                else:
                    string_to_remove = string_to_remove.replace(character,'')
                    tracker.discard(character)
            return string_to_remove

if __name__ == '__main__':
    #print remove_duplicates('my name is jeff')
    print remove_duplicates('aaabb')
