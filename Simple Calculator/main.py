from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  num1 = float(input("What's the first number?: "))
  end_cal = False
  
  count = 0
  end_answer = 0
  while not end_cal:
    for symbol in operations:
      print(symbol)
    
    operation_symbol = input("Pick an operation: ") 
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    
    if count == 0:
      
      answer = calculation_function(num1, num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    if count > 0 :
      answer = calculation_function(end_answer, num2)
      
      print(f"{end_answer} {operation_symbol} {num2} = {answer}")
  
    
    choice = input(f"If you wanna continue with {answer}'y' or else press 'n' for a new calculator ").lower()
    if choice == "n":
      end_cal = True
      calculator()

    count+=1
    end_answer = answer
    

calculator()
