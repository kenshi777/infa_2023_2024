import datetime
def log_func_call(log_file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            result = func(*args, **kwargs)
            end_time = datetime.datetime.now()
            execution_time = end_time - start_time

            with open(log_file, "a") as file:
                file.write(f"Время вызова функции: {start_time}\n")
                file.write(f"Входящие аргументы: args={args}, kwargs={kwargs}\n")
                file.write(f"Ответ return: {result if result is not None else '-'}\n")
                file.write(f"Время завершения работы функции: {end_time}\n")
                file.write(f"Время работы функции: {execution_time}\n\n")

            return result

        return wrapper

    return decorator

@log_func_call("log.log")
def example(a, b):
    return a + b

result = example(2, 3)
