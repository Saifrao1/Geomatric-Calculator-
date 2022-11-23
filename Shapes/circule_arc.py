
from math import pi


angle = float(input("Enter the angle value : "))
radius = float(input("Enter the Radius value : "))
# formulaes

area = pi * pow(radius, 2) * angle / 360
peri = (2 * pi) * radius * angle / 360

design = "~"*30
output = f"""
Output: 
{design}

Area = {area:.2f}
Perimeter  = {peri:.2f}

{design}
"""
print(output)
