import datetime

def get_user_info():
    name = input("👋 Hi there! What's your name? ")
    try:
        age = int(input("📅 How old are you? "))
        years_ahead = int(input("⏳ How many years into the future do you want to look? "))
        return name, age, years_ahead
    except ValueError:
        print("❌ Please enter valid numbers for age and years.")
        return None, None, None

def calculate_future_age(age, years_ahead):
    return age + years_ahead

def display_result(name, age, years_ahead, future_age, current_year):
    future_year = current_year + years_ahead
    print(f"\n🎉 Nice to meet you, {name}!")
    print(f"You are currently {age} years old in {current_year}.")
    print(f"In {years_ahead} years (in {future_year}), you will be {future_age} years old. 🕰️")

def main():
    current_year = datetime.datetime.now().year
    name, age, years_ahead = get_user_info()

    if name and age is not None and years_ahead is not None:
        future_age = calculate_future_age(age, years_ahead)
        display_result(name, age, years_ahead, future_age, current_year)

if __name__ == "__main__":
    main()
