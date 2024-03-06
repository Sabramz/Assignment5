import ast

class BasicMathOperations:
  
  @staticmethod
  def greet_user(first, last):
    print("Hello, " + first + " " + last + ".")
  
  @staticmethod
  def add():
    num1 = float(input("Enter a number "))
    num2 = float(input("Enter a number "))
    return num1 + num2
  
  @staticmethod
  def perform_operation(num1, num2, op):
    return eval(str(num1) +  op  + str(num2))
  
  @staticmethod
  def calculateSquare(num):
    return num * num
  
  def factorial(self, num):
    if num == 1 or num == 0:
      return 1
    else:
      return num * self.factorial(num - 1)

  def count(self, start, end):
    if start == end:
      print(end)
    else:
      print(start)
      self.count(start + 1, end)
    
  def calculateHypotenuse(self, base, perpendicular):
    return (self.calculateSquare(base) + self.calculateSquare(perpendicular)) ** 0.5
  
  @staticmethod
  def rectangle_area(base, height):
    return base * height
  
  @staticmethod
  def pow(base, exp):
    return base ** exp
  
  @staticmethod
  def type_of(thing):
    try:
      return type(ast.literal_eval(thing))
    except:
      return str


def main():
  bmo = BasicMathOperations()

  print("1: Greet user")
  print("2: Add two numbers")
  print("3: Perform operation on two numbers")
  print("4: Square a number")
  print("5: Compute a factorial")
  print("6: Count from one number to another")
  print("7: Calculate the hypotenuse of a right triangle")
  print("8: Calculate the area of a rectangle")
  print("9: Calculate the power of a number")
  print("10: Get the type of something")
  print("h: display the commands again")
  print("e: exit program")
  while True:

    userInput = input("Enter your next command: " )

    if userInput == "h":
      print("1: Greet user")
      print("2: Add two numbers")
      print("3: Perform operation on two numbers")
      print("4: Square a number")
      print("5: Compute a factorial")
      print("6: Count from one number to another")
      print("7: Calculate the hypotenuse of a right triangle")
      print("8: Calculate the area of a rectangle")
      print("9: Calculate the power of a number")
      print("10: Get the type of something")
      print("h: display the commands again")
      print("e: exit program")
      continue
    elif userInput == "e":
      print("Exiting...")
      break

    try: 
      userInput = int(userInput)
      if userInput == 1:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        bmo.greet_user(first_name, last_name)
      elif userInput == 2:
        print(bmo.add())
      elif userInput == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        op = input("Enter the operation (+, -, *, or /): ")
        while op not in ["+","-","*","/"]:
          op = input("Invalid operation. Enter one of +, -, *, or /: ")
        print(bmo.perform_operation(num1, num2, op))
      elif userInput == 4:
        num = float(input("Enter number to square: "))
        print(bmo.calculateSquare(num))
      elif userInput == 5:
        num = int(input("Enter number to compute factorial: "))
        if num >= 0:
          print(bmo.factorial(num))
        else:
          print("Cannot compute factorial of negative number " + str(num))
      elif userInput == 6:
        num1 = int(input("Enter number to count from: "))
        num2 = int(input("Enter number to count to: "))
        if num1 <= num2:
          bmo.count(num1, num2)
        else:
          print("Cannot count to a number less than " + str(num1))
      elif userInput == 7:
        num1 = float(input("Enter the length of the base: "))
        num2 = float(input("Enter the length of the perpendicular: "))
        if num1 <= 0:
          print("Invalid length " + str(num1))
        elif num2 <= 0:
          print("Invalid length " + str(num2))
        else:
          print(bmo.calculateHypotenuse(num1, num2))
      elif userInput == 8:
        num1 = float(input("Enter the width: "))
        num2 = float(input("Enter the height: "))
        if num1 <= 0:
          print("Invalid with " + str(num1))
        elif num2 <= 0:
          print("Invalid height " + str(num2))
        else:
          print(bmo.rectangle_area(num1, num2))
      elif userInput == 9:
        base = float(input("Enter the base: "))
        exp = float(input("Enter the exponent: "))
        print(bmo.pow(base, exp))
      elif userInput == 10:
        userIn = input("Enter the thing to get the type of: ")
        print(bmo.type_of(userIn))
      else:
        print("Input is not an option. Try again. Press h for help.")
    except:
      print("Input is not an option. Try again. Press h for help.")


main()