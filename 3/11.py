def decorator_maker():
    print("Я создаю декораторы! Я буду вызван только раз: когда ты попросишь меня создать декоратор.")
    def my_decorator(func):
        print("Я - декоратор! Я буду вызван только раз: в момент декорирования функции.")
        def wrapped():
            print ("Я - обёртка вокруг декорируемой функции.\n"
                   "Я буду вызвана каждый раз, когда ты вызываешь декорируемую функцию.\n"
                   "Я возвращаю результат работы декорируемой функции.")
            return func()
        print("Я возвращаю обёрнутую функцию.")
        return wrapped
    print("Я возвращаю декоратор.")
    return my_decorator

# Давайте теперь создадим декоратор. Это всего лишь ещё один вызов функции
new_decorator = decorator_maker()
# Теперь декорируем функцию
def decorated_function():
    print("Я - декорируемая функция.")

decorated_function = new_decorator(decorated_function)
# Теперь наконец вызовем функцию:
decorated_function()