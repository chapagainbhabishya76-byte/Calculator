print("")
print("")
print("==============CALCULATOR=============")
print("")
print("")
num1 = int(input("Enter 1st number : "))
operator = input("Enter calculating operator : ")
num2 = int(input("Enter 2nd number : "))

if (operator == "+"):
    print(num1 + num2)
elif (operator == "-"):
    print(num1 - num2)
elif (operator == "*"):
    print(num1 * num2)
elif (operator == "/"):
    print(num1 / num2)
elif (operator == "//"):
    print(num1 // num2)
elif (operator == "^"):
    print(num1 ** num2)