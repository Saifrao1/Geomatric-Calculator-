
side = float(input("Enter the Sides of a square: "))

area = pow(side, 2)
perimeter = side * 4


design = "~"*30
output = f"""
{design}

Area  = {area:.2f}
Perimeter  = {perimeter:.2f}

{design}

"""
print(output)
