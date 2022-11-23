side_A = float(input("Enter the side of A : "))
side_B = float(input("Enter the side of B : "))

# Formulaes
area = side_A * side_B
perimeter = (2 * side_A) + (2 * side_B)


# outputs
design = "^" * 30
output = f"""
{design}

Area  = {area:.2f}
Perimeter  = {perimeter:.2f}

{design}

"""
print(output)
