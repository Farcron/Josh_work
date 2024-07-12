# Step 1: Prompt the user to enter a temperature value
user_temperature_input = float(input("Enter the temperature value: "))

# Step 2: Prompt user to enter the unit (C for Celsius or F for Fahrenheit)
user_unit_input = input("Enter the unit (C Celsius or F for Fahrenheit): ").strip().upper()

# Step 3: Check the unit and perform the appropriate conversion
if user_unit_input == "C":
    # Step 3a: Convert Celsius to Fahrenheit
    converted_temperature = (9/5) * user_temperature_input + 32
    # Step 3b: Print the converted temperature in Fahrenheit
    print(f"The temperature in Fahrenheit is: {converted_temperature:.2f}")

elif user_unit_input == "F":
    # Step 4a: Convert Fahrenheit to Celsius
    converted_temperature = (5/9) * (user_temperature_input - 32)
    # Step 4b: Print the converted temperature in Celsius

    print(f"The temperature in Celsius is: {converted_temperature:.2f}")
else:
    # Step 7a: Print an error message indicating an invalid unit
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
