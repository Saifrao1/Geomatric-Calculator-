import math
from math import sqrt, pi
from re import A


side_a = float(input("Enter te valuse of side A : "))
side_b = float(input("Enter te valuse of side B : "))


def hypotenuse(first, second):
    g_powers = pow(first, 2) + pow(second, 2)
    hypo = sqrt(g_powers)
    hypo = hypo.real
    hypo = round(hypo, 2)
    return hypo


def angle(x, y):
    arc = x / y
    arc = float(f"{arc:.2f}")
    arcsin = math.asin(arc)
    arcsin = arcsin.real
    arcsin = float(f"{arcsin:.2f}")
    a_angle = 180 * arcsin / pi
    a_angle = round(a_angle, 2)
    return a_angle


def area(x, y):
    a_area = x * y / 2
    a_area = round(a_area, 2)
    return a_area


def perimeter(x, y, z):
    peri = x + y + z
    peri = round(peri, 2)
    return peri


h_hypotenuse = hypotenuse(side_a, side_b)
angle_a = angle(side_b, h_hypotenuse)
angle_b = angle(side_a, h_hypotenuse)
a_area = area(side_a, side_b)
p_perimeter = perimeter(side_a, side_b, h_hypotenuse)

design = "-"*30
output = f"""
{design}

Hypotenuse =  {h_hypotenuse}
Angle of A = {angle_a}\N{degree sign}
Angle of B = {angle_b}\N{degree sign}
Area  = {a_area}
Perimeter =  {p_perimeter}
{design}

"""
print(output)
