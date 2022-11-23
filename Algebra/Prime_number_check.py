
rng_from = int(input("Enter the Number from: "))
rng_to = int(input("Enter the Number To: "))
pr = int(input("Enter the Prime Number: "))


listno = []
list2 = []

for num in range(rng_from, rng_to+3):
    if(num % 2 != 0):
        listno.append(num)
    elif (num % 2 == 0):
        list2.append(num)


if pr in listno:
    if pr == 1:
        a = False
    else:
        a = True
        prime = listno.index(pr) + 1
        per_prime = listno.index(pr) - 1
        next_prime = listno[prime]
        per_prime = listno[per_prime]

elif pr in list2:
    a = False


if a:
    output = f"""
    OUTPUTS
    {"~"*30}

    {pr} is a Prime Number ?  {a}

    Next Prime Number is: {next_prime}

    Privious Prime Number is: {per_prime}

    {"~"*30}

    """
    print(output)
else:
    output = f"""
    {"~"*30}

    {pr} is a Prime Number ? :  {a}

    {"~"*30}

    """
    print(output)
