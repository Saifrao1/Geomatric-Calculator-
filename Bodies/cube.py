# INPUTS
side = float(input("Enter the value of a cube : "))

# FORMULES
total_area = 6 * pow(side, 2)
lateral_area = 4 * pow(side, 2)
volume = pow(side, 3)

# OUTPUTS
design = "^"*30
output = f"""
OUTPUTS
{design}

Total Area = {total_area:,.2f}
Leteral Area  = {lateral_area:,.2f}
Vloume =  {volume:,.2f}

{design}
"""
print(output)
