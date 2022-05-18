def longest_increasing_subsequence(score):
    if not score: #for empty score
        return score
    M = [None] * len(score)    # store an index of seq
    P = [None] * len(score)    # point to M
    # marks the length of longest incresing subsequence found up
    L = 1
    M[0] = 0
    # Looping over the sequence starting from the second element
    for i in range(1, len(score)):
        # hence we want the lower bound at the end of the search process.
        lower = 0
        upper = L
        # binary search will not look at the upper bound value, So we'll have to check that manually
        if score[M[upper-1]] < score[i]:
            j = upper
        else:
            # binary search loop
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if score[M[mid-1]] < score[i]:
                    lower = mid
                else:
                    upper = mid
            j = lower #using longest value
        P[i] = M[j-1]
        if j == L or score[i] < score[M[j]]:
            M[j] = i
            L = max(L, j+1)
    # Building the result
    result = []
    pos = M[L-1]
    for _ in range(L):
        result.append(score[pos])
        pos = P[pos]
    return result[::-1]    # reversing the result
