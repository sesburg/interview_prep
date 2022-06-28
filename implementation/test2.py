from Q4_4 import *

n, m = 5, 5
x, y, f = 2, 2, 0
world = [[1, 1, 1, 1, 1],[1, 1, 0, 1, 1], [1, 0, 0, 0, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1]]

set_world_global(world)
move(x, y, f)
print("expected result is 5")
print("Result:" + str(return_result()))

#Note: I don't think this is the best way to handle global variables, but it worked