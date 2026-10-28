import random

print("\t\tВыберите число от 1 до 100.\n\n")
r = random.randint(0,100)
c = 1
while (True):
    a = int(input("{}-я полытка  : ".format(c)))
    if (a > r):
        print("\033[93mмного ...\033[0m\n")
    elif (a < r):
        print("\033[94mмало ...\033[0m\n")
    else:
        print("\033[92mОтлично, вы угадали число; я загадал именно его. {} :)\033[0m\n".format(a))
        break
    c += 1