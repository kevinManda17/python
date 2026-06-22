def temp_c_to_f(temp_c):
    """Convert temperature from Celsius to Fahrenheit."""
    return round((1.8 * temp_c)+ 32, 2)

# ask user for an input temperature in celsius 
temp_c = float(input("Enter the temperature in celsius: \n"))

#convert temperature from celsius to farenheit 
temp_f = temp_c_to_f(temp_c)

#return the fahrenheit temperature to the user 
print(f"Temperature in Fahrenheit: {temp_f} F")