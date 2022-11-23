
from math import pi, sqrt


ra = float(input("Enter the value of Radius A: "))
rb = float(input("Enter the value of Radius B: "))
rc = float(input("Enter the value of Radius C: "))

#


def area(a, b, c):
    are = (pow((a*b), 1.6) + pow((a*c), 1.6) + pow((b*c), 1.6)) / 3
    are = (4 * pi) * (are ** (1/1.6))
    return are


def volume(a, b, c):
    vol = ((4 * pi) * a * b * c) / 3
    return vol


v_vol = volume(ra, rb, rc)
a_are = area(ra, rb, rc)
output = f""""

RESULTS
{"~"*30}

Area  = {a_are:,.2f}
Volume  = {v_vol:,.2f}

{"~"*30}

"""
print(output)
