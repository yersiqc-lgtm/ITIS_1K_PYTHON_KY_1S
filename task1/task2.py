#task
i = 0.1
final = 2
paso = 0.2
while (i <= final):
    print("{}".format(round(i,2)),", " if i < final-paso else "",end="")
    i += paso