# Step 1: Prompt the user to enter a length in centimeters
user_input = float(input("Enter a length in centimeters: "))

# Step 2: Check if the user input is negative
if user_input < 0:
    # Step 3a: If negative, print an error message
    print("Invalid entry.")
else:
    # Step 4a: If non-negative, convert the length to inches
    length_in = user_input / 2.45
    # Step 4b print the converted length
    print(f"The length in inches is: {user_input:.2f}")
