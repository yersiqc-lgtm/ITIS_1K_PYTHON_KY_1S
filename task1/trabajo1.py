############## task 1

import math

l = int(input("Dat : "))
G = 9.81
T = 2 * math.pi * math.sqrt(l//G)
print("result : {}".format(T))