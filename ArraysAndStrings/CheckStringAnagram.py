# Chapter 1 - Arrays and Strings
# 1.4
# Write a method to decide if two strings are anagrams or not.

def is_string_anagram(string1,string2):
    if isinstance(string1,str) and isinstance(string2,str):      
        if len(set(string1)) == len(set(string2)):
            return True
        else:
            return False

if __name__ == '__main__':
    print is_string_anagram('iceman','cinema')

