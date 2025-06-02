import datetime
import random
from colorama import Fore, Style, init

init(autoreset=True)  # Auto-reset colors after each print

fun_facts = [
    "Did you know? The human brain starts slowing down at around age 24!",
    "Fun fact: Your bones stop growing in length during your 20s.",
    "Aging gracefully is an art – and you're the artist!",
    "By age 30, your body starts losing muscle mass if you don’t exercise.",
    "Every 10 years, your taste buds replace themselves!"
]

def get_input(prompt, input_type=int):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(Fore.RED + "❌ Invalid input. Please try again.")

def get_user_info():
    name = input(Fore.CYAN + "👤 What's your name? (or type 'exit' to quit): ").strip()
    if name.lower() == 'exit':
        return None, None, None
    
    name = name.title()

    age = get_input(Fore.YELLOW + "📅 How old are you? ")
    years_ahead = get_input(Fore.YELLOW + "⏳ How many years into the future do you want to calculate? ")

    return name, age, years_ahead

def calculate_future_age(age, years_ahead):
    return age + years_ahead

def display_result(name, age, years_ahead, future_age, current_year):
    future_year = current_year + years_ahead
    birth_year = current_year - age

    print(Fore.GREEN + f"\n🎉 Hello, {name}!")
    print(f"🗓️ You were likely born in {birth_year}.")
    print(f"📍 You are {age} years old in {current_year}.")
    print(f"🚀 In {years_ahead} years (in {future_year}), you'll be {future_age} years old.")

    print(Fore.MAGENTA + f"\n💡 {random.choice(fun_facts)}\n")

def main():
    print(Fore.BLUE + Style.BRIGHT + "🎈 Welcome to the Supercharged Future Age Calculator!\n")
    current_year = datetime.datetime.now().year

    while True:
        name, age, years_ahead = get_user_info()
        if name is None:
            print(Fore.CYAN + "👋 Goodbye! Stay curious and take care!")
            break

        future_age = calculate_future_age(age, years_ahead)
        display_result(name, age, years_ahead, future_age, current_year)

if __name__ == "__main__":
    main()
