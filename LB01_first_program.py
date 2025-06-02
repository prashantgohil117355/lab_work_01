import datetime

# Get the current year
current_year = datetime.datetime.now().year

# Ask for user's name
name = input("What is your name? ")

# Ask for user's age with error handling
try:
    age = int(input("How old are you? "))
    future_age = age + 10
    future_year = current_year + 10

    # Display the result
    print(f"\nHello, {name}!")
    print(f"You are currently {age} years old in {current_year}.")
    print(f"In the year {future_year}, you will be {future_age} years old.")
except ValueError:
    print("Please enter a valid number for your age.")
