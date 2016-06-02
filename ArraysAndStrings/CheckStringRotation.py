"""
1.8
Assume you have a method isSubstring which checks if one word is a substring of
another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
only one call to isSubstring (i.e., 'waterbottle' is a rotation of 'erbottlewat').
"""

def isSubstring(word1,word2):
    return word1 in word2

def check_rotation(string1,string2):
    if len(string1) != len(string2):
        return False
    else:
        string2 += string2
        return isSubstring(string1,string2)

if __name__ == '__main__':
    assert (check_rotation('waterbottle','erbottlewat') == True)
    assert (check_rotation('apple','pplea') == True)
    assert (check_rotation('apple','ppale') == False)
