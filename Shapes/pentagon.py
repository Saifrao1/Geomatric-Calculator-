
from math import tan, pi


side = float(input("Enter the sides value : "))


def area(x):
    a1 = (x * (tan(54 * pi / 180))) / 4
    areas = pow(x, 2) * a1

    return areas


a_area = area(side)
peri = side * 5

output = f"""

Area = {a_area:.2f}
Perimeter  = {peri:.2f}

"""
print(output)
