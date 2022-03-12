#Program make a Simple Calculator

#This function adds two numbers
def add(a, b):
    return a + b

#This funtion subtracts two numbers
def subtract(a, b):
    return a - b

#This function multiplies two numbers
def multiply(a, b):
    return a*b

#This function divides two numbers
def divide(a, b):
    return a/b

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    #take input form the user
    choice = input("Enter choice [1; 2; 3; 4]")
    if choice in ('1', '2', '3', '4'):
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))

        if choice == '1':
            print(num_1, "+", num_2, add(num_1, num_2))

        elif choice == '2':
            print(num_1, "-", num_2, subtract(num_1, num_2))

        elif choice == '3':
            print(num_1, "*", num_2, multiply(num_1, num_2))

        elif choice == '4':
            print(num_1, "/", num_2, divide(num_1, num_2))

        #Check, If user wants another calculation
        #break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no)")
        if next_calculation == "no":
            break
    else:
        print("Invalid input")