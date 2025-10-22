from datetime import datetime 

birthdate=input("tug'ilgan sanangizni to'liq kiriting:")

birthdate=datetime.strptime(birthdate,"%Y-%m-%d")
today = datetime.today()

difference=today-birthdate
print(f"siz yashagan kunlar soni {difference.days}")




from datetime import datetime, date

birth_input = input("Tug'ilgan sanangizni kiriting (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_input, "%Y-%m-%d").date()
today = date.today()
next_birthday = birth_date.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)
days_left = (next_birthday - today).days
print(f"Sizning keyingi tug'ilgan kuningizgacha {days_left} kun qoldi ")

from datetime import datetime, timedelta
import pytz, time

# Meeting Scheduler
start_input = input("Hozirgi sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
start_time = datetime.strptime(start_input, "%Y-%m-%d %H:%M")
hours = int(input("Uchrashuv davomiyligi (soat): "))
minutes = int(input("Qo'shimcha daqiqa (agar bo'lsa, yo'q bo'lsa 0): "))
end_time = start_time + timedelta(hours=hours, minutes=minutes)
print(f"Uchrashuv tugash vaqti: {end_time.strftime('%Y-%m-%d %H:%M')}")

# Timezone Converter
date_str = input("\nSana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
from_tz_str = input("Hozirgi timezone (masalan: Asia/Tashkent): ")
to_tz_str = input("Qaysi timezone'ga o‘tkazmoqchisiz (masalan: Europe/London): ")
from_tz = pytz.timezone(from_tz_str)
to_tz = pytz.timezone(to_tz_str)
local_time = from_tz.localize(datetime.strptime(date_str, "%Y-%m-%d %H:%M"))
converted_time = local_time.astimezone(to_tz)
print(f"{to_tz_str} vaqti: {converted_time.strftime('%Y-%m-%d %H:%M')}")

# Countdown Timer
future_str = input("\nKelajakdagi sana va vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")
future = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")
while True:
    now = datetime.now()
    diff = future - now
    if diff.total_seconds() <= 0:
        print("⏰ Vaqt tugadi!")
        break
    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"\rQolgan vaqt: {days} kun, {hours:02d}:{minutes:02d}:{seconds:02d}", end="")
    time.sleep(1)


import re

# Email Validator
email = input("Email kiriting: ")
if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
    print("✅ To‘g‘ri email manzil.")
else:
    print("❌ Noto‘g‘ri email manzil.")

# Phone Number Formatter
phone = input("\nTelefon raqam kiriting (faqat raqamlar): ")
if re.match(r'^\d{10}$', phone):
    formatted_phone = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    print("Formatlangan raqam:", formatted_phone)
else:
    print("❌ Raqam 10 ta sondan iborat bo‘lishi kerak.")

# Password Strength Checker
password = input("\nParol kiriting: ")
if (len(password) >= 8 and
    re.search(r'[A-Z]', password) and
    re.search(r'[a-z]', password) and
    re.search(r'\d', password)):
    print("✅ Kuchli parol.")
else:
    print("❌ Parol kamida 8 ta belgidan iborat bo‘lishi, bitta katta harf, kichik harf va raqam o‘z ichiga olishi kerak.")

# Word Finder
text = """Python is an amazing programming language. 
Python helps in data analysis, web development, and automation."""
word = input("\nQidirilayotgan so‘zni kiriting: ").lower()
matches = [m.start() for m in re.finditer(word, text.lower())]
if matches:
    print(f"'{word}' so‘zi {len(matches)} marta uchradi. Indekslar: {matches}")
else:
    print(f"'{word}' so‘zi topilmadi.")

# Date Extractor
user_text = input("\nMatn kiriting (masalan: Bugun 22-10-2025 yoki 2025/10/22): ")
dates = re.findall(r'\b\d{2}[-/]\d{2}[-/]\d{4}\b|\b\d{4}[-/]\d{2}[-/]\d{2}\b', user_text)
if dates:
    print("Topilgan sanalar:", dates)
else:
    print("Sana topilmadi.")
