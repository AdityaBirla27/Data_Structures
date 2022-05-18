import math

def inner_product(L1,L2,domain):
    """
    Inner product between two vectors, where vectors
    are represented as alphabetically sorted (word,freq) pairs.

    Example: inner_product([["and",3],["of",2],["the",5]],
                           [["and",4],["in",1],["of",1],["this",2]]) = 14.0
    """
    sum = 0.0

    for each in domain:
        i = 0
        j = 0
        while i<len(L1):
            # L1[i:] and L2[j:] yet to be processed
            if L1[i][0] == each:
                while j<len(L2):
                    if L2[j][0]==each:
                        sum += L1[i][1] * L2[j][1]
                        break
                    else:
                        j=j+1
                break
            else:
                i=i+1
    return sum

def vector_angle(L1,L2):
    """
    The input is a list of (word,freq) pairs, sorted alphabetically.
    Return the angle between these two vectors.
    """
    domain=set()
    k=set()
    for each in L1:
        (x,y)=each
        domain.add(x)
    for each in L2:
        (a,b)=each
        k.add(a)
    domain=domain.intersection(k)
    numerator = inner_product(L1,L2,domain)

    denominator = math.sqrt(inner_product(L1,L1,domain)*inner_product(L2,L2,domain))
    return math.acos(numerator/denominator)
