# Chapter 1 - Arrays and Strings
# 1.2
# Write code to reverse a C-Style String. (C-String means that "abcd" is represented as
# five characters, including the null character.)

def reverse_string(string_to_reverse):
    return string_to_reverse[::-1] # [begin:end:step]

def reverse_string_v2(string_to_reverse):
    return ''.join(reversed(string_to_reverse))

if __name__ == '__main__':
    print reverse_string('my name is jeff \n')
    print reverse_string_v2('learning python \n')