def generate():
        values = [1, 2]

        for value in values:
            try:
                yield value

            except GeneratorExit as e:
                # При попытке выработать значение в ходе обработки 
                # поднимется RuntimeError.
                # yield 200  # RuntimeError: generator ignored GeneratorExit
                print('Принудительная остановка')
                raise  # Повторно поднимаем исключение.


my_generator = generate()

print(next(my_generator))  # 1


my_generator.close()  # Принудительная остановка
