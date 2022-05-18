#!/usr/bin/python
import sys
d = {}#empty dictionary to save values
def make_change(denominations, C):
    if C==0: return []# if 0 then return empty list
    for x in range(1, C+1):#for each element between 1 to C+1(subproblems) is necessary as this value is being used in future for easy calculations
        val = m(denominations,x) #for recusively calculating
    return (val[1])

# m is size of coins array (number of
# different coins)
def m(denominations,C):
    if C in d.keys():
        return d[C]
    elif C > 0:
        choices = [(m(denominations,C - x)[0] + 1, m(denominations,C - x)[1] + [x]) for x in denominations if C >= x] #recusively calculating
        # given a list of tuples, python's min function
        # uses the first element of each tuple for comparison
        d[C] = min(choices)
        return d[C]
    else:
        d[0] = (0, [])
        return d[0]
