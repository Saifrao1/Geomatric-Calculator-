print("FIND { RATIO } , {NUMERATOR}, {DENOMINATOR}")
a = float(input("Enter the value OF A: "))
b = float(input("Enter the value OF A: "))


class Ratio:
    def __init__(self, a, b):
        self.a_value = a
        self.b_value = b

    def ratio(self):
        r = self.a_value / self.b_value
        pass
