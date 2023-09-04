S = int(input("Initial savings: "))

P = int(input("Intrest procentage: "))

Y = int(input("Years of saving: "))

p2 = P/100 + 1

V =  S * p2 ** Y

print(round(V))    