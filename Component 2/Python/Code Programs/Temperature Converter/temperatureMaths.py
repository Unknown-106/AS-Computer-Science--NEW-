# temperatureMaths
# Azhi Amin
# 05/10/2026
# OCR AS Computer Science


# Returns the converted starting temperature from Farenheit to Celcius.
def Farenheit_Celcius(start_temp):
    try:
        return f"{(start_temp - 32) / (9 / 5):.5}*C"
    except Exception as e:
        print("Error occurred:", e)


# Returns the converted starting temperature from Celcius to Farenheit.
def Celcius_Farenheit(start_temp):
    try:
        return f"{(start_temp * (9 / 5)) + 32:.5}*F"
    except Exception as e:
        print("Error occurred:", e)
