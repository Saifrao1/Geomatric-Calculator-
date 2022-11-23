""" Linear Equation """

# a_value = float(input("Enter the value of A:\n"))
# b_value = float(input("Enter the value of B:\n"))

# # formula to calulate the x value {linear Equation  ax + b = 0}

# x_value = int(-(b_value/a_value))


# output = f"""

# Value of a is = {a_value}
# Value of b is = {b_value}
# Value of x is = {x_value}

# """
# print(output)


""" Quadratic Equation """


from cmath import sqrt
a_value = float(input("Enter the value of a:\n"))
b_value = float(input("Enter the value of b:\n"))
c_value = float(input("Enter the value of c:\n"))


# first find the formula of {b^2-4(ac)} then  finde the square root

finite = sqrt(int(b_value**2 - (4 * a_value * c_value)))
# finite = float(f"{finite: .2f}")


# find the valuse of x  {x =  -b + finite / 2 *a }
upper_value = float(-b_value + finite)


lower_value = int(2 * a_value)

# x_value = -(b_value) + finite / 2 * a_value
x_value = upper_value / lower_value

# x_value = -(b_value) - finite / 2 * a_value
upper_value2 = float(-b_value - finite)
x2_value = upper_value2 / lower_value

output = f"""

Value of a :  {a_value}
Value of b :  {b_value}
Value of c :  {c_value}

Value of X1 = {x_value:.2f}
Value of X2 = {x2_value:.2f}

"""
print(output)
