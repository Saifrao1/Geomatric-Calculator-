from math import sqrt


side_A = float(input("Enter the side of A : "))
side_B = float(input("Enter the side of B : "))
height = float(input("Enter the height : "))

# Formulaes
s = sqrt(pow((side_A - side_B) / 2, 2) + pow(height, 2))
s = round(s, 2)

area = (side_A + side_B) * height / 2
perimeter = (2 * s) + (side_A + side_B)

# outputs
design = "^" * 30
output = f"""
{design}

Area  = {area:.2f}
Perimeter =  {perimeter:.2f}

{design}

"""
print(output)
