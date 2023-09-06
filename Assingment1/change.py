price = float(input("Price: "))
payment = float(input("Payment: "))

change = round(payment - price)
print("Change: ", change)

kr1000 = change//1000
kr500 = (change - kr1000 * 1000) // 500
kr200 = (change - kr1000 * 1000 - kr500 * 500) // 200
kr100 = (change - kr1000 * 1000 - kr500 * 500 - kr200 * 200) // 100
kr50 = (change - kr1000 * 1000 - kr500 * 500 - kr200 * 200 - kr100 * 100) // 50
kr20 = (change - kr1000 * 1000 - kr500 * 500 - kr200 * 200 - kr100 * 100 - kr50 * 50) // 20
kr10 = (change - kr1000 * 1000 - kr500 * 500 - kr200 * 200 - kr100 * 100 - kr50 * 50 - kr20 * 20) // 10
kr5 = (change - kr1000 * 1000 - kr500 * 500 - kr200 * 200 - kr100 * 100 - kr50 * 50 - kr20 * 20 - kr10 * 10) // 5
kr2 = (change - kr1000 * 1000 - kr500 * 500 - kr200 * 200 - kr100 * 100 - kr50 * 50 - kr20 * 20 - kr10 * 10 - kr5 * 5) // 2
kr1 = (change - kr1000 * 1000 - kr500 * 500 - kr200 * 200 - kr100 * 100 - kr50 * 50 - kr20 * 20 - kr10 * 10 - kr5 * 5 - kr2 * 2) // 1

if price > payment:
    print("You're too broke")

print("1000kr bills: ", kr1000)
print("500kr bills: ", kr500)
print("200kr bills: ", kr200)
print("100kr bills: ", kr100)
print("50kr bills: ", kr50)
print("20kr bills: ", kr20)
print("10kr bills: ", kr10)
print("5kr bills: ", kr5)
print("2kr bills: ", kr2)
print("1kr bills: ", kr1)