"""
8.7
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and
pennies (1 cent), write code to calculate the number of ways of representing n cents.

O(N!) time?
"""
QUARTERS = 25
DIMES = 10
NICKELS = 5
PENNIES = 1

CENTS = [PENNIES, NICKELS, DIMES, QUARTERS]

def getAllCombinationOfNCents(N, tracker = []):
    if N == 0:
        return [tracker]
    else:
        result = []
        for coin in CENTS:
            newTracker = list(tracker)
            if N >= coin:
                newTracker.append(coin)
                for newPath in getAllCombinationOfNCents(N - coin, newTracker):
                    result.append(newPath)
        return result

def numOfReprOfNCents(N):
    result = []
    listOfAllCombinations = getAllCombinationOfNCents(N)
    for i in listOfAllCombinations:
        i.sort()
        if i not in result:
            result.append(i)
            print i
    return len(result)


test = numOfReprOfNCents(35)
print test


