from math import sqrt


a = float(input("Enter the side A value : "))
b = float(input("Enter the side B value : "))
h = float(input("Enter the height H value : "))

# FORMULAES


def l_area(a, b, h):
    l_areas = (2 * (a + b)) * sqrt(pow(h, 2) + pow(((b - a) / 2), 2))

    return l_areas


def total_area(l, a, b):
    t_area = l + pow(a, 2) + pow(b, 2)
    return t_area


def volume(a, b, h):
    v = (pow(a, 2) + a * b + pow(b, 2)) * h / 3
    return v


# OUTPUTS
lateral_area = l_area(a, b, h)
t_area = total_area(lateral_area, a, b)
t_volume = volume(a, b, h)

design = "~" * 30
output = f"""
OUTPUTS
{design}

Lateral Area = {lateral_area:.2f}
Total Area = {t_area:.2f}
Volume = {t_volume:.2f}

{design}
"""
print(output)
