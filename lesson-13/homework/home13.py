import re
from datetime import datetime, timedelta
import time
import pytz
import email.utils


def age_calculator():
    birth_date = input("Enter your birthdate (YYYY-MM-DD): ")
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.today()

    delta = today - birth_date
    years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    months = (today.year - birth_date.year) * 12 + today.month - birth_date.month
    days = delta.days

    print(f"Age: {years} years, {months % 12} months, {days} days")


def days_until_next_birthday():
    birth_date = input("Enter your birthdate (YYYY-MM-DD): ")
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.today()
    next_birthday = birth_date.replace(year=today.year)

    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    delta = next_birthday - today
    print(f"Days until next birthday: {delta.days} days")


def meeting_scheduler():
    current_time = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
    hours = int(input("Enter meeting duration hours: "))
    minutes = int(input("Enter meeting duration minutes: "))
    current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")
    end_time = current_time + timedelta(hours=hours, minutes=minutes)
    print(f"Meeting will end at: {end_time.strftime('%Y-%m-%d %H:%M')}")


def timezone_converter():
    date_time_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    from_tz_str = input("Enter current timezone (e.g., Asia/Tashkent): ")
    to_tz_str = input("Enter target timezone (e.g., Europe/London): ")

    local = pytz.timezone(from_tz_str)
    target = pytz.timezone(to_tz_str)

    local_dt = local.localize(datetime.strptime(date_time_str, "%Y-%m-%d %H:%M"))
    target_dt = local_dt.astimezone(target)

    print(f"Time in {to_tz_str}: {target_dt.strftime('%Y-%m-%d %H:%M')}")


def countdown_timer():
    future_time_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
    future_time = datetime.strptime(future_time_str, "%Y-%m-%d %H:%M:%S")

    while True:
        now = datetime.now()
        if now >= future_time:
            print("Time's up!")
            break

        delta = future_time - now
        print(f"Time remaining: {delta}", end="\r")
        time.sleep(1)


def email_validator():
    email_input = input("Enter an email address: ")
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email_input):
        print("Valid email address.")
    else:
        print("Invalid email address.")


def phone_formatter():
    number = input("Enter a 10-digit phone number: ")
    clean = re.sub(r'\D', '', number)
    if len(clean) == 10:
        print(f"Formatted: ({clean[:3]}) {clean[3:6]}-{clean[6:]}")
    else:
        print("Invalid number. Must contain 10 digits.")


def password_strength_checker():
    password = input("Enter a password: ")
    strength = {
        "length": len(password) >= 8,
        "uppercase": re.search(r'[A-Z]', password),
        "lowercase": re.search(r'[a-z]', password),
        "digit": re.search(r'\d', password)
    }
    if all(strength.values()):
        print("Strong password.")
    else:
        print("Weak password. Requirements not met:")
        for key, value in strength.items():
            if not value:
                print(f"- Missing {key}")


def word_finder():
    text = "This is a simple test text. This text is just a sample. Test it thoroughly."
    word = input("Enter the word to find: ").lower()
    matches = [m.start() for m in re.finditer(rf"\b{word}\b", text.lower())]

    if matches:
        print(f"Word '{word}' found {len(matches)} times at positions: {matches}")
    else:
        print("Word not found.")


def date_extractor():
    text = input("Enter a text containing dates: ")
    dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text)
    if dates:
        print("Found dates:", dates)
    else:
        print("No dates found.")
