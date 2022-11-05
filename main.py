# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y

#Need to define divide function.
def divide (x,y):
    return x/y

print("Calculator started.")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 


finish_state = False # 계산 종료를 위한 상태값

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            
        elif choice =='4':
            print(num1, "/", num2, "=", divide(num1,num2))
            

        # check if user wants another calculation
        # break the while loop if answer is no
        while True:
            next_calculation = input("Let's do next calculation? (yes/no): ")
            next_calculation = next_calculation.lower() # 모든 문자열을 소문자로 변환시켜줌
            if next_calculation == "no":
                finish_state = True
                break
            elif next_calculation == "why":
                continue
        
        if finish_state == True:
            break

    else:
        print("Invalid Input")