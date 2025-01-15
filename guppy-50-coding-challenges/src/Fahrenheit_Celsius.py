# Create a function that will convert from Fahrenheit to Celsius
input = float(input("Enter the temperature in Fahrenheit: "))
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
print(f"The temperature in Celsius is: {fahrenheit_to_celsius(input)}")
