
#Ugly numbers only have 2, 3, 5 as their prime factors
#return nth ugly number
def uglyNumber(n):
    dp = [0] * n 
    dp[0] = 1
    idx2 = idx3 = idx5 = 0
    twos = 2
    threes = 3
    fives = 5
    for i in range(1, n):
        dp[i] = min(twos, threes, fives)
        if dp[i] == twos:
            idx2 += 1
            twos = dp[idx2] * 2
        if dp[i] == threes:
            idx3 += 1
            threes = dp[idx3] * 3
        if dp[i] == fives:
            idx5 += 1
            fives = dp[idx5] * 5
    return dp[n - 1]

n = 4
print(uglyNumber(n))




    
