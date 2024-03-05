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
    if start == end + 1:
      return end
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

