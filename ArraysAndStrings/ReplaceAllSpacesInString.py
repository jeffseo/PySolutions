# Chapter 1 - Arrays and Strings
# 1.5
# Write a method to replace all spaces in a string with '%20'
# 

def replace_all_spaces(string):
    return string.replace(' ','%20')

def replace_all_spaces_v2(string):
    return_string = ''
    for character in string:
        if character == ' ':
            return_string += '%20'
        else:
            return_string += character
    return return_string


if __name__ == '__main__':
    print replace_all_spaces('my name is jeff')
    print replace_all_spaces_v2('my name is jeff')