from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multipy(n1,n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multipy,
  "/" : divide,  
}

def calculator():
  print(logo)
  num1 = float(input("What is the first number? "))
  for operation in operations:
    print(operation)
   
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number? "))
    
    calculation = operations[operation_symbol]
    answer = calculation(num1, num2)
  
    print(f'{num1} {operation_symbol} {num2} = {answer}')
    
    if input(f"Type 'Y' to continue calculating with {answer}, or type 'N' to start a new calculation. ").lower() == "y":
      num1 = answer 
    else: 
      should_continue = False
      calculator()

calculator()


#print(f'{num1} {operation_symbol} {num2} = {answer}')