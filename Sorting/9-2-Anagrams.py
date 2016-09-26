"""
9.2
Write a method to sort an array of strings so that all the anagrams are next to each
other.

"""

# method 1. use ascii
# method 2. sort the alphabets in the string and compare if equall
def getAscii(string):
    value = 0
    for char in string:
        value += ord(char)
    return value

def SortAnagrams(array):
    return sorted(array, key=getAscii)

test = ['olleh','suck','cusk','kek','bob','boob','hello']
print SortAnagrams(test)