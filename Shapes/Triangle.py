from math import acos, pi, sqrt

a = int(input("ENter the le8ft-side value of A\n"))
b = int(input("ENter the ground value of B\n"))
c = int(input("ENter the right-side value of C\n"))

# formula {A+B+C/2}
s = float((a + b + c) / 2)
print(s)

# find the Area of a triangle
area = sqrt(s * ((s-a) * (s - b) * (s - c)))
area = area.real

# find the perimeter { A + B + C}
perimeter = int((a + b + c))


# Angle of AB
# first find the | arccos x { A^2 + B^2 - C^2 / 2 x ( a x b)} |
# for angle of AB
def powersAB(a, b, c):
    """_retuen Powers of given values_

    Args:
        a (_int_): _get from users_
        b (_int_): _get from users_
        c (_int_): _get from users_

    Returns:
        _float_: _Powwers of A,B,C and doing some math_
    """
    powers_ab = pow(a, 2) + pow(b, 2) - pow(c, 2)
    return powers_ab


def powersBC(a, b, c):
    """_retuen Powers of given values_

    Args:
        a (_int_): _get from users_
        b (_int_): _get from users_
        c (_int_): _get from users_

    Returns:
        _float_: _ power_bc _
    """
    powers_bc = pow(b, 2) + pow(c, 2) - pow(a, 2)
    return powers_bc


def powersAC(a, b, c):
    """_retuen Powers of given values_

    Args:
        a (_int_): _get from users_
        b (_int_): _get from users_
        c (_int_): _get from users_

    Returns:
        _float_: _ Powers_ab _
    """
    powers_ac = pow(a, 2) + pow(c, 2) - pow(b, 2)
    return powers_ac


def lower(first, second):
    l = 2 * (first * second)
    return l


def angles(upper, bottom):
    arccos = upper / bottom

    # # Find the value of Acos using python method acos()
    arccos = acos(arccos)

    # # value of acos is complex number convert into real number
    arccos = arccos.real
    arccos = float(f"{arccos:.2f}")

    # # next  divide this value to pi and multiply to 180
    angle_ab = arccos / pi
    angle_ab = float(angle_ab * 180)

    return angle_ab


def height(a_area, h_height):
    h = (2 * a_area) / h_height
    return h


angles_ab = angles(powersAB(a, b, c), lower(a, b))
angles_bc = angles(powersBC(a, b, c), lower(b, c))
angles_ac = angles(powersAC(a, b, c), lower(a, c))
height_a = height(area, a)
height_b = height(area, b)
height_c = height(area, c)

design = "*" * 30


output = f"""
{design}

Araa = {area:.2f}
Perimeter  = {perimeter}
Angle of AB = {angles_ab:.2f}\N{DEGREE SIGN}
Angle of BC = {angles_bc:.2f}\N{DEGREE SIGN}
Angle of AC = {angles_ac:.2f}\N{DEGREE SIGN}
Height of A = {height_a:.2f}
Height of B = {height_b:.2f}
Height of C = {height_c:.2f}

{design}
"""
print(output)
