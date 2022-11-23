from math import sqrt, pi


r = float(input("Enter the valuse of Radius: "))
h = float(input("Enter the valuse of Height: "))


def lat_area(r, h):
    l = 2 * pi
    return l


def area(l, r):
    a = l + (pi * pow(r, 2))
    return a


def volume(r, h):
    v = (pi * pow(r, 2)) * h / 3
    return v


# OUTPUTS
l_lat_area = lat_area(r, h)
a_area = area(l_lat_area, r)
v_volume = volume(r, h)
design = "^"*30
output = f"""
OUTPUTS:
{design}

Lateral Area = {l_lat_area:,.2f} 
Total Area = {a_area:,.2f}
Volume = {v_volume:,.2f}

{design}
"""
print(output)
