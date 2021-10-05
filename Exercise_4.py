from math import pi
for i in range(2, 12):
    text = "Pi = {:." + str(i) + "f}"
    print(text.format(pi))