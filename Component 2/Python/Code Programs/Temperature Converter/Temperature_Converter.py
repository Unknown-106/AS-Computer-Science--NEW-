# Temperature Converter
# Azhi Amin
# 05/10/2026
# OCR AS Computer Science


# Standard Libraries
import inspect

# Third-Party Libraries
pass

# Local Modules
import temperatureMaths


# The primary user interface (UI) that appears when the program is run. It also uses some Defensive Programming to prevent ValueErrors
def main_menu():
    try:
        option = input(inspect.cleandoc("""
            Welcome to the Temperature Converter for Celcius and Farenheit

            
            Which direction would you like to convert in?

            For Farenheit to Celcius, type 'Y'
            For Celcius to Farenheit, type 'N'

            :
        """))
        while option != "Y" and "N":
            option = input("Please type 'Y' or 'N':")
        try:
            start_temp = float(
                input("Input your starting temperature as a decimal number:")
            )
        except ValueError:
            while start_temp != float:
                try:
                    start_temp = float(
                        input(
                            "Error. Please input your starting temperature as a decimal number:"
                        )
                    )
                except ValueError:
                    pass
        return option, start_temp
    except Exception as e:
        print("Error occurred:", e)


# Runs some conditional logic that determines which function from the temperatureMaths conversion module needs to run and runs it, returning the converted temperature with units.
def conversion(option, start_temp):
    try:
        if option == "Y":
            end_temp = temperatureMaths.Farenheit_Celcius(start_temp)
        elif option == "N":
            end_temp = temperatureMaths.Celcius_Farenheit(start_temp)
        return end_temp
    except Exception as e:
        print("Error occured:", e)


# Takes the result of the conversion calculation and outputs the start temperature and the converted temperature.
def result(start_temp, end_temp):
    try:
        print(inspect.cleandoc(f"""
            __Conversion complete__
        
            {start_temp} converts to {end_temp}.
        """))
    except Exception as e:
        print("Error occured:", e)


# Main execution sequence.
def main():
    try:
        option, start_temp = main_menu()
        end_temp = conversion(option, start_temp)
        result(start_temp, end_temp)
    except Exception as e:
        print("Error occurred:", e)


# program starts here
if __name__ == "__main__":
    main()
