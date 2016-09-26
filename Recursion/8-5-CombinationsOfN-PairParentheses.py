"""
8.5
Implement an algorithm to print all valid (e.g., properly opened and closed) combinations
of n-pairs of parentheses.
EXAMPLE:
input: 3 (e.g., 3 pairs of parentheses)
output: ()()(), ()(()), (())(), ((()))

We can solve this problem recursively by recursing through the string. On each iteration, we
have the index for a particular character in the string. We need to select either a left or a right
paren. When can we use left, and when can we use a right paren?
- Left: As long as we haven't used up all the left parentheses,
        we can always insert a left paren
- Right: We can insert a right paren as long as it won't lead to a syntax error. 
        When will we get a syntax error?
        We will get a syntax error if there are more right parentheses than left
"""

def printParentheses(numOfPairs, string = []):
    numOfLeftParan = string.count('(')
    numOfRightParan = string.count(')')
    if numOfLeftParan < numOfRightParan:
        return

    if (numOfLeftParan == numOfPairs and numOfRightParan == numOfPairs):
        print ''.join(string)
    else:
        if numOfLeftParan < numOfPairs: #try a left paren
            newString = string + ['(']
            printParentheses(numOfPairs, newString)
        if numOfRightParan < numOfPairs and numOfRightParan < numOfLeftParan:
            newString = string + [')']
            printParentheses(numOfPairs, newString)

printParentheses(3)