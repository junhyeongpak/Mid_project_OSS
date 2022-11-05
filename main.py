# Program make a simple calculator

from calc_lib import *

print("Calculator started.")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 


finish_state = False # 계산 종료를 위한 상태값

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

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
            # 분모에 0이 들어오는 경우 계산을 실행하이 않는다. 
            if num2 == 0:
                print("Do not divide by zero!!!")
            # 0이 아닌 경우는 정상적으로 divide를 실행한다.
            else:
                print(num1, "/", num2, "=", divide(num1,num2))
            

        # check if user wants another calculation
        # break the while loop if answer is no
        while True:
            next_calculation = input("Let's do next calculation? (yes/no): ")
            next_calculation = next_calculation.lower() # 모든 문자열을 소문자로 변환시켜줌
            if next_calculation == "no":
                # 종료 루프 개선
                check = input("Are you sure? (yes/no)")
                check = check.lower()
                # 정말 종료 할시 종료
                if check == "yes":
                    finish_state = True
                    break
                # no라고 대답할 경우 다시 Enter choice로 회귀함
                else:
                    break
            # 재확인 루틴 기능 추가
            elif next_calculation == "why?":
                continue
            # 다음 계산을 하는 경우 Enter choice로 회귀함
            elif next_calculation == "yes":
                break
            # 그 외의 이상한 답변이 오는 경우 다시 Let's do next calc로 회귀
            else:
                print("Please anwser...(yes/no)")
                continue
        
        if finish_state == True:
            break

    else:
        print("Invalid Input")