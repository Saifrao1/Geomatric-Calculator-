

from math import pi, sqrt

radius_a = float(input("Enter the value of Radius A: "))
radius_b = float(input("Enter the value of Radius B: "))


area = pi * (radius_a * radius_b)
peri = sqrt((pow(radius_a, 2) + pow(radius_b, 2)) / 2)
peri = (2 * pi) * peri

design = "~" * 30
output = f"""
OUTPUT
{design}

Area = {area:.2f}
Perimeter = {peri:.2f}

{design}

"""
print(output)
