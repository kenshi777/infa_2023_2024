def decorator(func_to_decorate):
    def the_wrapper():
        print("Работаю до вызова функции")
        func_to_decorate()
        print("Срабатываю после")
    return the_wrapper

@decorator
def func_based():
    print('Hey bro')

func_based()