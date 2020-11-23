def some_list(s):
    return print(s().split())

@some_list
def some_str():
    return input("Введите какую-нибудь строку: ")