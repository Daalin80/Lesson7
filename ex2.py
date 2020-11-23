def celcium():
    t = int(input("Введите температуру: "))
    print("По Кельвину; ", round((t - 273.15), 2))
    print("По Фаренгейту: ", round(((t - 32) / 1.8), 2))

def kelvin():
    t = int(input("Введите температуру: "))
    print("По Цельсию: ", round((t + 273.15), 2))
    print("По Фаренгейту: ", round(((t + 459.67) / 1.8), 2))

def farengate():
    t = int(input("Введите температуру: "))
    print("По Кельвину: ", round(((t * 1.8) - 459.67), 2))
    print("По Цельсию: ", round(((t * 1.8) + 32), 2))

temp_type = input("Введите тип температуры C, K или F: ")
if temp_type == "C":
    celcium()
elif temp_type == "K":
    kelvin()
elif temp_type == "F":
    farengate()

