x = int(input("Insert the numerator: \n"))
y = int(input("Insert the denomiator: \n"))

if x%y == 0:
    print(x, " is divisible by ", y)
else:
    print("No! " ,x, " is not divisible by ", y)