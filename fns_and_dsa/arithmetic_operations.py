def perform_operation(num1:float, num2:float, operation:str)->float:
       if operation == "add":
              return num1 + num2
       elif operation == "subtract":
              return num1 - num2
       elif operation == "multiply":
              return num1 * num2
       elif operation == "divide":
              if num2 != 0:
                     return num1 / num2
              else: return "Error cannot divide by zero"
       else:
              return "Invalid operation"
       
num1 = float(input("Enter the first Number "))
num2 = float(input("Enter the first Number "))
operation = input("Enter the operation(add, subtract,multiply,divide): ")
result =perform_operation(num1,num2,operation)
print ("Result", result)