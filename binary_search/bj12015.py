import sys
from bisect import bisect_left

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

#상상도 못한 풀이다..
#Key idea: The important part is the LENGTH
#so LIA doesn't have to accurately represent the longest increasing array
#it just needs to maintain the length of the best subarray found so far
#We do it by substituting the current value after 
#the largest number in LIA that is smaller than current value
#ex) lia = [10, 20, 30], num = 15 -> lia = [10, 15, 30]
#Even though [10, 15, 30] is not valid subarray (15 appeared after 30),
#it doesn't matter because the length 3 is still the best solution so far.

#find the length of the longest increasing sub-array
lia = []  #longest increasing subarray
for num in arr:
    if len(lia) == 0:
        lia.append(num)
    elif lia[-1] < num:
        lia.append(num)
    elif lia[-1] > num:
        idx = bisect_left(lia, num)      
        lia[idx] = num

print(len(lia))

