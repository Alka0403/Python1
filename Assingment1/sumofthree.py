#VG
D = int(input("Provide a three digit number: "))

q = D%10
w = D//10
e = w%10
r = w//10

sum = q + e + r

print("Sum of digits: ", sum)