income = int(input("Please provide monthly income: "))

if income <= 38000:
    q = income * .3
    print("Corresponding income tax: ", q)
elif income <= 50000:
    q = income - 38000
    w = 38000 * .3
    e = q * .35
    r = w + e
    print("Corresponding income tax: ", r)
elif income > 50000:
    q = income - 50000
    w = 38000 * .3
    e = 12000 * .35
    r = q * .4
    t = w + e + r
    print("Corresponding income tax: ", t)