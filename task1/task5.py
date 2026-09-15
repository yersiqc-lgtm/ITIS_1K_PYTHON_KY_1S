# homework
import random

while(True):
    num_row = int(input("Введите основание треугольника: "))
    if num_row%2 == 0:
        print("\033[93mERROR\033[0m")
    else: 
        break

u_desc = num_row

for i in range(1,num_row+1,2):
    print(" "*(u_desc//2),end="")
    for j in range(i):
        print("\033["+str(random.randint(31,37))+"m*",end='')
    print()
    u_desc -= 2
