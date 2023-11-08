import json
import math
import csv

text = "игра 0+"
print(text.upper())

def save_to_csv(name, age):
        with open('user_data_play.csv', mode='a', newline='', encoding='utf-8') as file:
           writer = csv.writer(file)
           writer.writerow([name, age])
           
def greet():
    name = input("Введите ваше имя: ")
    age = input("Введите ваш возраст: ")
    parameters = {
        "name": name,
        "age": age
    }

    with open("parameters.json", "w") as json_file:
        json.dump(parameters, json_file)

    print("Добро пожаловать в игру,", name + "!")
    print("Игра: Придумайте себе завтрак")
    print("Начинаем игру!!!")

    



def choose_action():
    print("Выбирите ваш будущий завтрак:")
    print("1. Яичница")
    print("2. Бутерброды")
    print("3. Доставка еды")

    choice = input("Введите номерок будущего завтрака: ")
    return choice

def fried_egg():
    print("Готовим яичницу")
    print("Выбираем наполнение яичнецы: яйцо и бекон, яйцо и сыр, яйцо и помидоры")

    content = ["яйцо и бекон", "яйцо и сыр", "яйцо и помидоры"]
    choice_content = []

    while True:
        print("\nНаполнение яичнецы, которую вы выбрали:", ", ".join(choice_content))
        action = input("Можем поменять выбор или 'жарить' для приготовления яйчницы: ")
        if action == "жарить":
            break

        if action in content:
            choice_content.append(action)
            content.remove(action)
            print(f"Вы выбрали {action} ,чтобы пожарить яичнецу.")

    print("\nУряя яичница готова!")
    print("Давайте кушааать")

def sandwich():
    print("Готовим бутерброды")
    print("Выбираем вид бутерброда: французский с круассаном, итальянская чиаббатта с беконом, русский со шпротами")

    type_of = ["французский с круассаном", "итальянская чиаббатта с беконом", "русский со шпротами"]
    type_of_sandwich = []

    while True:
        print("\nВид бутерброда, который вы выбрали:", ", ".join(type_of_sandwich))
        action = input("Можем поменять вид продукты или 'собирать бутерброд' для приготовления бутерброда: ")
        if action == "собирать бутерброд":
            break

        if action in type_of:
            type_of_sandwich.append(action)
            type_of.remove(action)
            print(f"Вы выбрали {action} ,чтобы приготовить бутерброд.")

    print("\nУряя бутерброды готовы!")
    print("Давайте завтракать")

def ordering_dish():
    print("Вы зашли в яндекс доставку, где предлагаются разнообразные блюда.")
    print("Выберите, что бы вы хотели заказать на романтическтй вечер: салат, сырники с сгущенкой, каша с ягодами, йогурт с злаками")

    menu = {
        "салат": 300,
        "сырники с сгущенкой": 400,
        "каша с ягодами": 400,
        "йогурт с ягодами":320
    }

    choice_dishes = []

    while True:
        print("\nВаши выбранные блюда:", ", ".join(choice_dishes))

        dish = input("Введите название блюда или 'оплатить' для завершения заказа: ")
        if dish == "оплатить":
            break

        if dish in menu:
            choice_dishes.append(dish)
            print(f"Вы заказали {dish}.")
        else:
            print("Такого блюда нет в меню. Попробуйте снова.")

    total_cost = sum(menu[блюдо] for блюдо in choice_dishes)

    print("\nВы завершили заказ в яндекс доставке, ожидайте заказ!")
    print("Ваши выбранные блюда:", ", ".join(choice_dishes))
    print("Сумма заказа:", total_cost, "руб.")

def greet1():
    greet()
    while True:
        action = choose_action()
        if action == "1":
            fried_egg()
        elif action == "2":
            sandwich()
        elif action == "3":
            ordering_dish()
        else:
            print("Некорректная команда. Пожалуйста, попробуйте снова.")
            continue 

        with open("parameters.json", "r") as json_file:
            data = json.load(json_file)
            name, age = data["name"], data["age"]       
        save_to_csv(name, age) 
greet1()