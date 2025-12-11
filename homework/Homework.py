import json

data = {
    "Model": "Malibu",
    "Rang": "Qora",
    "Yil": 2020,
    "Narh": 40000
}


data_json = json.dumps(data, ensure_ascii=False, indent=4)
print(data_json)




talaba_json = {
{"ism":"Hasan","familiya":"Husanov","tyil":2000}
}

talaba = json.loads(talaba_json)

print("Ism:", talaba["ism"])
print("Familiya:", talaba["familiya"])


[
    {"ism": "Ali", "familiya": "Karimov", "kurs": 2, "fakultet": "Dasturiy injiniring"},
    {"ism": "Madina", "familiya": "Xolova", "kurs": 1, "fakultet": "Kimyo"},
    {"ism": "Javlon", "familiya": "Usmonov", "kurs": 3, "fakultet": "Iqtisodiyot"}
]





with open("talabalar.json", "r", encoding="utf-8") as f:
    talabalar = json.load(f)

for t in talabalar:
    print(f"{t['ism']} {t['familiya']}, {t['kurs']}-kurs, {t['fakultet']} talabasi")


print("Ali Karimov, 2-kurs, Dasturiy injiniring talabasi")
print("Madina Xolova, 1-kurs, Kimyo talabasi")
print("Javlon Usmonov, 3-kurs, Iqtisodiyot talabasi")
