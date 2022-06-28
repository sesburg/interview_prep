from Q4_4 import *

n, m = 5, 6
world = [[1, 1, 1, 1, 1, 1],\
         [1, 0, 0, 1, 0, 1], \
         [1, 0, 0, 0, 1, 1],\
         [1, 1, 0, 1, 1, 1], \
         [1, 1, 1, 1, 1, 1]]
set_world_global(world)

move(2, 1, 0)
print("Test: expected result is 4")
print("Result:" + str(return_result()))

reset_test()
move(2, 3, 3)
print("Test: expected result is 6")
print("Result:" + str(return_result()))

#Note: I don't think this is the best way to handle global variables, but it worked