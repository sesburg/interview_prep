def devide(a, b):
    if a < 0:
        return -((-a) // b)
    else:
        return a // b

res = []
def dfs(idx, val, oper):
    global most, least
    if idx == n:
        most = max(most, val)
        least = min(least, val)
    else:
        for i in range(4):
            if oper[i] > 0:
                oper[i] -= 1
                if i == 0:
                    dfs(idx + 1, val + numbers[idx], oper)
                if i == 1:
                    dfs(idx + 1, val - numbers[idx], oper)
                if i == 2:
                    dfs(idx + 1, val * numbers[idx], oper)
                if i == 3:
                    dfs(idx + 1, devide(val,numbers[idx]), oper)
                oper[i] += 1
                
n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

most, least = -1e10, 1e10
dfs(1, numbers[0], operators)
print(most)
print(least)