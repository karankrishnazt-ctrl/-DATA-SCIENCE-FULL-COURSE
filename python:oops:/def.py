# _____________________Demonstrates defining a function with a parameter_______________________________________
# def hello(to): 
#      print("hello,", to)

# name = input("What's your name? ") 
# hello(name)


#______________ Demonstrates defining a function with a parameter with a default value__________________
class Calculator:
    @staticmethod
    def add(x,y):
        return x+y
    
    @staticmethod
    def subtract(x,y):
        return x-y
Calculator.add(6,5)
    