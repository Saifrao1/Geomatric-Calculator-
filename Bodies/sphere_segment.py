from math import pi
a = float(input("Enter the value of Radius A : "))
r = float(input("Enter the value of Radius R : "))
h = float(input("Enter the value of Height H : "))


class Spehere_segment:
    def __init__(self, a, r, h):
        self.radius_a = a
        self.radius_r = r
        self.height = h

    def volume(self):

        v = ((pi * self.height)/6) * ((3 * pow(self.radius_a, 2)) +
                                      (3 * pow(self.radius_r, 2)) + pow(self.height, 2))
        return v


volumes = Spehere_segment(a, r, h)
# print(volumes.volume())

# this don by calling method by class name
print(f" Volume = {Spehere_segment.volume(volumes):,.2f}")
