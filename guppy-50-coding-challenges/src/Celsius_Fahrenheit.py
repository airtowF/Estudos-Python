# Create a function that will convert from Celsius to Fahrenheit

input = float(input("Enter the temperature in Celsius: "))
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(f"The temperature in Fahrenheit is: {celsius_to_fahrenheit(input)}")