
from math import pi

r = float(input("Enter the value of Radius :"))
h = float(input("Enter the value of Height :"))


class Sphere_cap:
    def __init__(self, r, h):
        self.radius = r
        self.height = h

    def leteral_area(self):
        a = pi * (pow(self.radius, 2) + pow(self.height, 2))
        return a

    def total_area(self):
        ta = (result.leteral_area() + (pi * pow(self.radius, 2)))
        return ta

    def volume(self):
        # v = (3*pi*self.height) * \
        #     ((pow(self.radius, 2)) + pow(self.height, 2))
        # v /= 6

        v = (1/6 * pi * self.height) * \
            ((3 * pow(self.radius, 2)) + pow(self.height, 2))

        return v


result = Sphere_cap(r, h)
output = f"""
Leteral Area =  {result.leteral_area():,.2f}
Total Area   =  {result.total_area():,.2f}
Volume       =  {result.volume():,.2f}

"""
print(output)
