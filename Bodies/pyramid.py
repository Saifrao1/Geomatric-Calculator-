from math import sqrt


a = float(input("Enter the side A value : "))
h = float(input("Enter the height H value : "))

# FORMULAES
l_area = (2 * a) * sqrt(pow(h, 2) + pow((a/2), 2))
volume = pow(a, 2) * h / 3
area = l_area + (pow(a, 2))
# OUTPUTS
design = "~" * 30
output = f"""
OUTPUTS
{design}

Lateral Area = {l_area:.2f}
Total Area  = {area:.2f}
Volume  = {volume:.2f}

{design}
"""
print(output)
