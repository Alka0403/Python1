T = int(input("Give a number of seconds: "))

h = T//3600
t2 = T%3600
m = t2//60
s = t2%60

print("This corresponds to: ", h,"hours", m,"minutes and", s, "seconds")