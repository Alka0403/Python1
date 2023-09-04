import random

n = random.randint(-10,10)

r = "is even" if n % 2 == 0 else "is odd"

if n > 0:
    s = ("and positive")
elif n < 0:
    s = ("and negative")
elif n == 0:
    s = ("and neither positive nor negative")

print("The generated number is ", n)
print(n, r, s)