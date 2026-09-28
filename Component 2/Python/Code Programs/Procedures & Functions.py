# Procedures & Functions
# Azhi Amin
# 04/09/2026
# OCR AS Computer Science

#Simple procedure
def procedureName():
    try:
        print("Output here\n")
    except Exception as e:
        print("Error occurred:",e)

procedureName()


#Multiple procedures
def greeting():
    try:
        print("Hello there.")
    except Exception as e:
        print("Error occurred:",e)

def question():
    try:
        print("How are you?.")
    except Exception as e:
        print("Error occurred:",e)#

def farewell():
    try:
        print("Goodbye.")
    except Exception as e:
        print("Error occurred:",e)

greeting()
question()
farewell()


#Passing parameters
def outputName(forename, surname):
    try:
        print(f"Hello {forename} {surname}.")
    except Exception as e:
        print("Error occurred:",e)

#Calling the procedure <outputName> and passing in the parameter "Bob" and "Cratchit".
outputName("Bob","Cratchit")


#Arithmetic with parameters, using a function
def adding(num1,num2,num3):
    try:
        return num1 + num2 + num3
    except Exception as e:
        print("Error occurred:",e)

num1 = 1
num2 = 10
num3 = 100

#prints the returned value of the function <adding(num1,num2,num3))>
print(adding(num1,num2,num3))


#Functions Calculator

#...
def inputValue():
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    return num1,num2

#...
def exponent(num1,num2):
    return num1**num2

#...
def remainder(num1,num2):
    return num1%num2

#...
def floorDivision(num1,num2):
    return num1//num2

#...
def division(num1,num2):
    return num1/num2

#...
def multiplication(num1,num2):
    return num1*num2

#...
def subtraction(num1,num2):
    return num1-num2

#...
def addition(num1,num2):
    return num1+num2

#...
def outputValue(answer):
    print(answer)

#...
def calculator():
    answer = 1.0
    print("Calculator")
    inputValue()
    choice = input("Pick calculator function: ")
    if choice == "Exponent" or "exponent":
        answer = exponent(num1,num2)
    elif choice == "Remainder" or "remainder" or "MOD" or "mod" or "Modulus" or "modulus":
        answer = remainder(num1,num2)
    elif choice == "Floor Division" or "floor division" or "Floor" or "floor":
        answer = floorDivision(num1,num2)
    elif choice == "Division" or "division":
        answer = division(num1,num2)
    elif choice == "Multiplication" or "multiplication":
        answer = multiplication(num1,num2)
    elif choice == "Subtraction" or "subtraction":
        answer = subtraction(num1,num2)
    elif choice == "Addition" or "addition":
        answer = addition(num1,num2)
    outputValue(answer)

#calculator starts here
if (__name__ == "__main__"):
    calculator()


#...
def three():
    try:
        pass
    except Exception as e:
        print("Error occurred:",e)


#...
def main():
    try:
        pass
    except Exception as e:
        print("Error occurred:",e)

#program starts here
if (__name__ == "__main__"):
    main()
