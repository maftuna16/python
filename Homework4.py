filename = 'pi_million_digits.txt'
with open(filename, 'r') as file:
    pi_digits_str = file.read()
print(f"Fayldan {len(pi_digits_str)} ta belgi o'qildi.")



def is_birthday_in_pi(birthday_str, pi_str):
    if birthday_str in pi_str:
        return True
    else:
        return False


my_birthday = '06092009'

if is_birthday_in_pi(my_birthday, pi_digits_str):
    print(f"Sizning {my_birthday} tug'ilgan sanangiz Pi raqamlari ichidan topildi!")
else:
    print(f"Sizning {my_birthday} tug'ilgan sanangiz Pi raqamlari ichidan topilmadi.")




import pickle


pi_float = float(pi_digits_str)

with open('pi_float.pkl', 'wb') as file:
    pickle.dump(pi_float, file)

print("Pi raqamlari floatga o'tkazildi va pi_float.pkl fayliga pickle yordamida saqlandi.")