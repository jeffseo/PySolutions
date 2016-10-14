def convertStrToInt(string):
    integer = 0
    negative = False
    for itr, num in enumerate(string):
        if itr == 0 and not (ord(num) >= ord('0') and ord(num) <= ord('9')):
            if ord(num) == ord('-'):
                negative = True
                continue
        integer = integer * 10 + (ord(num) - ord('0'))
    if negative:
        integer = -integer
    return integer

print convertStrToInt("1234") 
print type(convertStrToInt("1234"))