a = float(input("Enter the value of side A: "))
b = float(input("Enter the value of side B: "))
c = float(input("Enter the value of side C: "))

# FORMULAES
area = (2 * (a * b)) + (2 * (b * c)) + (2 * (a * c))
lateral_area = (2 * (a * b)) + (2 * (a * c))
volume = a * b * c

# OUTPUTS
design = "~" * 30
output = f"""
OUTPUTS
{design}

Total Area  = {area:.2f}
Lateral Area  = {lateral_area:.2f}
Volume  = {volume:.2f}

{design}
"""
print(output)
