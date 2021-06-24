import time

if __name__ == '__main__':
    start_time = time.perf_counter()
    print(start_time)
    end_time = time.perf_counter()
    print(end_time - start_time)
