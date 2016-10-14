# Chapter 1 - Arrays and Strings
# 1.4
# Write a method to decide if two strings are anagrams or not.

# http://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/


# Sorts a string into a list of characters and checks if two are equal
def is_string_anagram(string1,string2):
    if isinstance(string1,str) and isinstance(string2,str):      
        return sorted(string1) == sorted(string2)

# sums up the individual character unicode values and checks if two are equal # NOTE: This does not work for certain cases e.g. "ac" "bb" returns true
def is_string_anagram_v2(string1,string2):
    if sum(ord(x) for x in string1) == sum(ord(x) for x in string2):
        return True
    else:
        return False

if __name__ == '__main__':
    print is_string_anagram('iceman','cinema')
    print is_string_anagram_v2('iceman','cinema')

