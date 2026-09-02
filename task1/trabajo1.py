############## version 1

T = (lambda l,PI,G:2 * PI * __import__("math").sqrt(l//G))(int(input()),__import__("math").pi,9.81)
print(T)

############## version 2 git puch

import math

l = int(input("Dat : "))
G = 9.81
T = 2 * math.pi * math.sqrt(l//G)
print("result : {}".format(T))