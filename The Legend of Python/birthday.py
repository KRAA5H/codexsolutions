from datetime import date as dt
import random

bday_messages = [
    "Hope you have a very Happy Birthday! 🎈",
    "It's your special day – get out there and celebrate! 🎉",
    "You were born and the world got better – everybody wins! 🥳",
    "Have lots of fun on your special day! 🎂",
    "Another year of you going around the sun! 🌞",
]

random_bday_message = random.choice(bday_messages)

next_birthday_input = input("Enter your birthday (YYYY-MM-DD): ")
next_birthday = dt.fromisoformat(next_birthday_input)

today_date = dt.today()
days_away = (next_birthday - today_date).days

if days_away == 0:
    print(random_bday_message)
