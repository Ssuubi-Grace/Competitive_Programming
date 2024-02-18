def isSubset(a1, a2, n, m):
    freq_a1 = {}
    for num in a1:
        freq_a1[num] = freq_a1.get(num, 0) + 1
    
    for num in a2:
        if num not in freq_a1 or freq_a1[num] == 0:
            return "No" 
        freq_a1[num] -= 1
    
    return "Yes" 
