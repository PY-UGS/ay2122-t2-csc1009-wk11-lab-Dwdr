class calculator:
    #Constructor
    def __init__(self,input1,input2):   
        self.input1 = input1
        self.input2 = input2
    #Function for addition
    def adder(self):
        return (self.input1 + self.input2)
    #Function for Subtraction
    def subtractor(self):
        return (self.input1 - self.input2)
    #Function for Multiplication
    def multiplier(self):
        return (self.input1 * self.input2)
    #Function for Division
    def divider(self):
        return (self.input1 / self.input2)
    #Function to clear inputs
    def clear(self):
        self.input1 = 0
        self.input2 = 0


input1 = input("Enter first number for input1: ")     #ask for first input1
input2 = input("Enter second number for input2: ")    #ask for second input2
input1 = float(input1)      #convert input1 from a float to integer
input2 = float(input2)      #convert input2 from a float to integer

calculatorobject = calculator(input1,input2)

print("Result for Addition of the two numbers is: " + str(calculatorobject.adder()))
print("Result for Subtraction of the two numbers is: " + str(calculatorobject.subtractor()))
print("Result for Multiplication of the two numbers is: " + str(calculatorobject.multiplier()))
print("Result for Division of the two numbers is: " + str(calculatorobject.divider()))
calculatorobject.clear()
print("Result after Clearing of the two numbers is: ( Input1 = " + str(calculatorobject.input1) + " ), ( Input 2 = " + str(calculatorobject.input2) + " )")