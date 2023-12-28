import random

def introduction():
    print("Добро пожаловать в игру 'Инвазия космических уток'!")
    print("Космические утки решили захватить Землю, и только ты можешь их остановить.")
    print("Выбирай защитные действия и спаси мир от утиной угрозы!")

def choose_defense():
    options = [
        "Запустить ракеты с кукурузой",
        "Использовать гигантский лазерный кот",
        "Активировать армию роботов-садовников",
        "Отправить на помощь отряд ниндзя-кроликов"
    ]
    print("\nКосмические утки атакуют! Как вы будете защищаться?")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    choice = int(input("Выберите действие (введите номер): ")) - 1
    return options[choice]

def battle_result(defense):
    results = [
        "Космические утки испугались и улетели!",
        "Утки оказались аллергиками на ваше оружие! Атака отражена!",
        "Утки нейтрализованы, но они отправили сигнал о помощи!",
        "О нет! Утки адаптировались к вашей защите!"
    ]
    print(f"Вы использовали {defense}.")
    print(random.choice(results))

def space_ducks_invasion():
    introduction()

    while True:
        defense = choose_defense()
        battle_result(defense)

        if input("\nПродолжить защиту? (да/нет): ").lower() != 'да':
            print("Спасибо за игру! Земля временно в безопасности.")
            break

space_ducks_invasion()