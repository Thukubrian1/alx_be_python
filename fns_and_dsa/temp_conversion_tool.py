FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = float(input("Enter the temperature to convert: "))


def convert_to_celsius():
        fahrenheit = (temperature - 32)  * FAHRENHEIT_TO_CELSIUS_FACTOR
        print(f"{temperature}°F is {fahrenheit}°C")

def convert_to_fahrenheit():
        celsius = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        print(f"{temperature}°C is {celsius}°F")
        

conversion = input("Is this temperature in Celsius or Fahrenheit? (C/F: ")

if conversion == "C":
        print(convert_to_fahrenheit())

elif conversion == "F":
        print(convert_to_celsius())

else:
        print("Invalid input")


