
from math import pi


radius = float(input("Enter the Radius value : "))
# formulaes
dia = radius * 2
area = pi * pow(radius, 2)
circum = (2 * pi) * radius


output = f"""
Diameter = {dia:.2f}
Area = {area:.2f}
Circumference  = {circum:.2f}

"""
print(output)
