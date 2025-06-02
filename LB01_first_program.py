import datetime

def get_user_info():
    name = input("👋 What's your name? (or type 'exit' to quit): ").strip()
    if name.lower() == 'exit':
        return None, None, None
    
    name = name.title()  # Capitalize name properly

    try:
        age = int(input("📅 How old are you? "))
        years_ahead = int(input("⏳ How many years into the future do you want to calculate? "))
        return name, age, years_ahead
    except ValueError:
        print("❌ Invalid input! Please enter numbers for age and years.\n")
        return None, None, None

def calculate_future_age(age, years_ahead):
    return age + years_ahead

def display_result(name, age, years_ahead, future_age, current_year):
    future_year = current_year + years_ahead
    print(f"\n🌟 Hello, {name}!")
    print(f"✅ You are {age} years old in {current_year}.")
    print(f"📈 In {years_ahead} years (in {future_year}), you will be {future_age} years old.\n")

def main():
    print("🧮 Welcome to the Future Age Calculator!\n")
    current_year = datetime.datetime.now().year

    while True:
        name, age, years_ahead = get_user_info()
        if name is None:
            print("👋 Goodbye! Have a great day!")
            break

        future_age = calculate_future_age(age, years_ahead)
        display_result(name, age, years_ahead, future_age, current_year)

if __name__ == "__main__":
    main()
