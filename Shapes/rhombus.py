from math import sqrt

a = float(input("Enter the valuse of A : "))
b = float(input("Enter the valuse of B : "))


def area(x, y):
    areas = (x * y) / 2
    return areas


def perimeter(x, y):
    peri = sqrt(pow(x/2, 2) + pow(y/2, 2)) * 4
    return peri


a_area = area(a, b)
a_peri = perimeter(a, b)

design = "~"*30
output = f"""
{design}

Area  = {a_area:.2f}
Perimeter  = {a_peri:.2f}

{design}
"""
print(output)
