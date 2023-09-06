input1 = input("Enter a chess square identifier (e.g. e5): ")
let = input1[0]
nmr = int(input1[1])


if let == 'a' and nmr % 2 == 0 or let == 'c' and nmr % 2 == 0 or let == 'e' and nmr % 2 == 0 or let == 'g' and nmr % 2 == 0:
    print(input1, "is white")
elif let == 'a' and nmr % 2 != 0 or let == 'c' and nmr % 2 != 0 or let == 'e' and nmr % 2 != 0 or let == 'g' and nmr % 2 != 0:
    print(input1, "is black")
elif let == 'b' and nmr % 2 != 0 or let == 'd' and nmr % 2 != 0 or let == 'f' and nmr % 2 != 0 or let == 'h' and nmr % 2 != 0:
    print(input1, "is white")
elif let == 'b' and nmr % 2 == 0 or let == 'd' and nmr % 2 == 0 or let == 'f' and nmr % 2 == 0 or let == 'h' and nmr % 2 == 0:
    print(input1, " is black")
else:
    print("enter again")