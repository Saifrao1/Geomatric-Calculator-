
from math import sqrt


side = float(input("Enter the sides value : "))


def area(x):
    a1 = (3 * sqrt(3)) / 2
    areas = pow(x, 2) * a1

    return areas


a_area = area(side)
peri = side * 6

output = f"""

Area = {a_area:.2f}
Perimeter  = {peri:.2f}

"""
print(output)
