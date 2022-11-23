from math import pi
r = float(input("Enter the radius : "))


class Radius:
    def __init__(self, r):
        self.userinput = r

    def area(self):
        area = (4 * pi) * pow(self.userinput, 2)
        return area

    def vloume(self):
        v = ((4 * pi) * pow(self.userinput, 3)) / 3
        return v


radius = Radius(r)
output = f"""

Area  =  {radius.area():,.2f}
Volume = {radius.vloume():,.2f}

"""
print(output)
