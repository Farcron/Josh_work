# Step 1: Prompt the user to enter a temperature value in Celsius
user_temperature_input = float(input("Enter the temperature in Celsius: "))

# Step 2: Check the temperature value and print the corresponding message
if user_temperature_input < -273.25:
    # Step 2a: Temperature is below absolute zero
    print("The temperature is invalid because it is below absolute zero.")

elif user_temperature_input == 273.15:
    # Step 3a: Temperature is absolute zero
    print("The temperature is absolute zero.")

elif -273.15 < user_temperature_input < 0:
    # Step 4a: Temperature is below freezing
    print("The temperature is below freezing.")

elif user_temperature_input == 0:
    # Step 5a: Temperature is at the freezing point
    print("The is at the freezing point.")

elif 0 < user_temperature_input < 100:
    # Step 6a: Temperature is in the normal range
    print("The temperature is in normal range.")

elif user_temperature_input == 100:
    # Step 7a: Temperature is at the boiling point
    print("The temperature is at the boiling point.")

elif user_temperature_input > 100:
    # Step 8a: Temperature is above the boiling point
    print("The temperature is above the boiling point.")
