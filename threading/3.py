import threading
import time

def calc(arr, start, end, result):
    partial_sum = sum(arr[start:end])
    result.append(partial_sum)


def calculate_sum_parallel(arr, num_threads):
    result = []
    threads = []

    chunk_size = len(arr) // num_threads
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(arr)

        thread = threading.Thread(target=calc, args=(arr, start, end, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(result)

if __name__ == "__main__":
    array = list(range(1, 1000001))  # Пример массива с числами от 1 до 1 миллиона

    for num_threads in [1, 2, 4, 8]:
        start_time = time.time()
        result = calculate_sum_parallel(array, num_threads)
        end_time = time.time()

        print(f"Number of threads: {num_threads}, Sum: {result}, Time: {end_time - start_time} seconds")