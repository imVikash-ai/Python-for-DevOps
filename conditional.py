day_of_week = input("Enter the day of the week: ").lower()

print("You entered: ", day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday":
    print("I will learn live DevOps")

else:
    print("I will practice DevOps")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


choice = input("Enter your operations:(Options: +, -, *, /, %) ")

if choice == "+":
    sum_of_number = num1 + num2
    print("Addition: ",sum_of_number)
elif choice == "-":
    diff_of_num = num1 - num2
    print("Subtraction: ",diff_of_num)
elif choice == "*":
    product_of_num = num1 * num2
    print("Multiplication: ",product_of_num)
elif choice == "/":
    division_of_num = num1 / num2
    print("Division: ",division_of_num)
elif choice == "%":
    remainer_of_number = num1 % num2
    print("Remainder: ",remainer_of_number)
else:
    print("Invalid choice")