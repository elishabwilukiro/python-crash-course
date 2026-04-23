print("Calculator\n")
operator = input("Select operator ( + - * / ): ")
number1 = float(input("Enter 1st number: "))
number2 = float(input("Enter 2nd number: "))

if(operator == "+"):
     result = number1 + number2
     print("Answer is ", round(result,2))
elif(operator == "-"):
     result = number1 - number2
     print("Answer is ", round(result,2))
elif(operator == "*"):
     result = number1 * number2
     print("Answer is ", round(result,2))
elif(operator == "/"):
     result = number1 / number2
     print("Answer is ", round(result,2))
else:
     print("Operator {operator} entered is invalid")
