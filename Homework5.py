from datetime import datetime, timedelta

bugun = datetime.today()

for i in range(10):
    sana = bugun + timedelta(weeks=2)
    print(sana.strftime("%Y-%m-%d"))


########
bugun = datetime.today()

ramazon_hayiti = datetime(2026, 3, 20)
qurbon_hayiti = datetime(2026, 5, 27)

for name, sana in [("Ramazon hayitiga", ramazon_hayiti), ("Qurbon hayitiga", qurbon_hayiti)]:
    farq = sana - bugun
    print(f"{name} qolgan kunlar: {farq.days}")




#######
import re

telefon = input("Telefon raqamingizni kiriting (+998 XX XXX XX XX): ")

andoza = r"^\+998\s?\d{2}\s?\d{3}\s?\d{2}\s?\d{2}$"

if re.match(andoza, telefon):
    print("Raqam to'g'ri!")
else:
    print("Raqam noto'g'ri!")





########
import re


telefon = input("Iltimos, telefon raqamingizni kiriting: ")


pattern = r'^(\+998|998)?(9[0-9])[0-9]{7}$'


if re.fullmatch(pattern, telefon):
    print("Telefon raqami to'g'ri.")
else:
    print("Telefon raqami noto'g'ri. Iltimos, +998901234567 formatida kiriting.")