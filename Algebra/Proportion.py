a = float(input("Enter the value of A:"))
b = float(input("Enter the value of B:"))
x = float(input("Enter the value of X:"))


class Proportionl:
    def __init__(self, a, b, x):
        self.a_value = a
        self.b_value = b
        self.x_value = x

    def directly_proportionl(self):
        y = (self.x_value * self.b_value) / self.a_value
        return y

    def indirectly_proportional(self):
        y = (self.a_value * self.b_value) / self.x_value
        return y


print("What you want to find ?")
dp = int(input("Enter 1 for Directly Proportionl and 2 for Indirectly Proportional:\n"))


if dp == 1:
    directly = Proportionl(a, b, x)
    output = f""""

    Directly Propotional
    {'^'*30}

    Value of Y is = {directly.directly_proportionl():,.2f} 

    {'^'*30}
    """
elif dp == 2:
    indirectly = Proportionl(a, b, x)
    output = f""""

    Indirectly Propotional
    {'^'*30}

    Value Of Y is  = {indirectly.indirectly_proportional():,.2f} 

    {'^'*30}
    """

print(output)
