# Sequence, Selection, Iteration
# Azhi Amin
# 9/9/2026
# OCR AS Computer Science

#Name Concatenation (Sequence)
def assignment():
    try:
        #assignment
        forename = input("What is your forename? ")
        surname = input("What is your surname? ")
        #output concatenation
        print("Hello" + ' ' + forename + ' ' + surname)
        print("Hello",forename,surname)
    except Exception as e:
        print("Error occurred:",e)

#A Farenheit-Celcius Bidirectional Converter (Sequence, Selection, Iteration, and High Defensive Programming)
def tempConversion():
    try:
        conversionDirection = "String"
        print("\nConverter: Celcius-Farenheit")
        while conversionDirection != "C" and conversionDirection != "c" and conversionDirection != "F" and conversionDirection != "f":
            conversionDirection = input("Converting from Celcius (C) or Farenheit (F)? ")
            if conversionDirection != "C" and conversionDirection != "c" and conversionDirection != "F" and conversionDirection != "f":
                print("Error. Try entering just C or F.\n")
        if conversionDirection == "F" or conversionDirection == "f":
            F = float(input("Temperature in Farenheit: "))
            C = (F-32)/1.8
            print(F,"degrees Farenheit converted to",C,"degrees Celcius.")
        elif conversionDirection == "C" or conversionDirection == "c":
            C = float(input("Temperature in Celcius: "))
            F = (C*1.8)+32
            print(C,"degrees Celcius converted to",F,"degrees Farenheit.")
        else:
            print("Error: Invalid input.")
    except Exception as e:
        print("Error occurred:",e)

#Unidirectional Converter of Seconds to Days|Hours|Minutes|Seconds (Sequence)
def convertSeconds():
    try:
        print("Converter: Seconds to Days|Hours|Minutes|Seconds")
        seconds = float(input("Enter seconds: "))
        days = seconds//86400
        secondsRemaining = seconds%86400
        hours = secondsRemaining//3600
        secondsRemaining = secondsRemaining%3600
        minutes = secondsRemaining//60
        secondsRemaining = round(secondsRemaining%60, 10)
        print(seconds,"seconds converts to",days,"Days",hours,"Hours",minutes,"Minutes",secondsRemaining,"Seconds.")
    except Exception as e:
        print("Error occurred:",e)

#sum of all numbers
def ForToWhile():
    try:
        n = 5 #number of terms
        sum_of_natural_numbers = 0
        number = 1
        
        while number in range (1, n + 1):
            sum_of_natural_numbers += number
            number += 1
            
        print(f"The sum of first {n} natural numbers is {sum_of_natural_numbers}.")
    except Exception as e:
        print("Error occurred:",e)

#Environmental Monitoring System
def EnvironmentalMonitoringSystem():
    try:
        import time

        #monitoring the temperature and humidity as they rise
        print("Environmental Monitoring System")

        temperature = 5 #Initial temperature in Celcius
        humidity = 20   #Initial humidity percentage

        while temperature < 30 and humidity < 70:
            print(f"Temperature: {temperature}*C | Humidity: {humidity}%")

            #Simulating changes in temperature and humidity
            temperature += 1
            humidity += 5

            time.sleep(0.5)

        print("Environmental conditions are outside the optimal range.")
        print("Please take necessary actions to adjust the environment.")
    except Exception as e:
        print("Error occurred:",e)

#Tree Growth Simulator
def TreeGrowthSimulator():
    try:
        print("Tree Growth Simulator")

        initialHeight = 1.0 #Initial height of the tree in metres
        growthRate = 0.99 # Annual growth rate in metres
        years = 0

        maxHeight = float(input("Enter max height (2 d.p): ")) #User enters a decimal for their required max height
        
        print(f"Starting with a tree height of {initialHeight} metres.")

        while initialHeight < maxHeight:
            years += 1
            initialHeight += growthRate

            print(f"Year {years}: Tree height is {initialHeight:.2f} metres.")

        print("The tree has reached its maximum height.")
    except Exception as e:
        print("Error occurred:",e)

        
#...
def main():
    try:
        assignment()
        tempConversion()
        convertSeconds()
        ForToWhile()
        EnvironmentalMonitoringSystem()
        TreeGrowthSimulator()
    except Exception as e:
        print("Error occurred:",e)

#program starts here
if (__name__ == "__main__"):
    main()
