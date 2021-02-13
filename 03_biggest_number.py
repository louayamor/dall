x = int(input("Insert the first number: "))
y = int(input("Insert the second number: "))
z = int(input("Insert the third number: "))

print("The biggest number is: ", end="")
if y <= x >= z:
    print(x)
elif y <= z >= x:
    print(z)
else:
    print(y)