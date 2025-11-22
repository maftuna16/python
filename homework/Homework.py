def user_data(first_name, last_name, age):
    print(f"Ism: {first_name}")
    print(f"Familiya: {last_name}")
    print(f"Yosh: {age}")


user_data("Alisher", "Olimov", 27)



def find_max(a, b, c):
    max_num = max(a, b, c)
    result = []

    if max_num == a:
        result.append("A")
    if max_num == b:
        result.append("B")
    if max_num == c:
        result.append("C")

    print(f"Eng katta son - {' va '.join(result)} = {max_num}")


find_max(10, 10, 5)



def find_letter_count(word, letter):
    count = word.lower().count(letter.lower())
    print(f'"{word}" so‘zida "{letter}" dan {count} ta.')


find_letter_count("Programing", "r")



def list_sum(myList):
    print("Listning elementlar yig‘indisi =", sum(myList))


list_sum([5, 7, 10, 10])




def daraja(a, b):
    print(a ** b)


daraja(2, 5)



def daraja4(a, b, c, d):
    print(a ** b)
    print(a ** c)
    print(a ** d)


daraja4(2, 2, 3, 4)





def digit_count_and_sum(word):
    total = 0
    count = 0
    for ch in word:
        if ch.isdigit():
            total += int(ch)
            count += 1
    print("Raqamlar soni:", count)
    print("Raqamlar yig‘indisi:", total)


digit_count_and_sum("ab12c3")






def add_right(a, b):
    print(int(str(a) + str(b)))


add_right(12, 45)   # 1245





def add_left(a, b):
    print(int(str(b) + str(a)))


add_left(12, 45)   # 4512




def work_with_list(a):
    min_val = min(a)
    new_list = [x * min_val for x in a]
    print(new_list)


work_with_list([5, 3, 7])





def big_sales(sales):
    return max(sales, key=sales.get)


sales = {
  "yanvar": 12000,
  "mart": 6000,
  "aprel": 15000,
  "sentabr": 9000,
  "dekabr": 10000,
}

print(big_sales(sales))




def min_max(numbers, max_num, min_num):
    real_max = max(numbers)
    real_min = min(numbers)

    print("Berilgan max to‘g‘rimi?", max_num == real_max)
    print("Berilgan min to‘g‘rimi?", min_num == real_min)


min_max([5, 9, 2, 11], 11, 2)




def expensiveProduct(products):
    max_price = -1
    expensive_name = ""

    for p in products:
        if p["price"] > max_price:
            max_price = p["price"]
            expensive_name = p["name"]

    print("Eng qimmat telefon:", expensive_name)


products = [
    {"name": "Iphone X", "price": 600},
    {"name": "Iphone 12", "price": 1500},
    {"name": "Samsung Note 9", "price": 800},
    {"name": "Samsung S10", "price": 1100},
]

expensiveProduct(products)