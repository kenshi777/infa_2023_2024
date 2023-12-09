def decorator(func_to_decorate):
    def the_wrapper():
        print("Работаю до вызова функции")
        func_to_decorate()
        print("Срабатываю после")
    return the_wrapper

def func():
    print("простая функция")

func()

# func_decorated = decorator(func)
# func_decorated()

func = decorator(func)
func()