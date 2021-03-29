"""
An Algorithm is a procedure or formula for solving some problem
"""

# Consider this def

def sum1(n):
    '''
    Take an input n and return sum of numbers fro 0 - n
    '''
    sum = 0
    for x in range(n+1): # Have to add 1 to get five actual nums. Range starts at 0
        sum += x

    return sum

print(sum1(5))

def sum2(n):
    # Same as above but different algo

    return (n*(n+1))/2

print(sum2(5))

# Objectively compare these 2 defs







