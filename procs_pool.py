import time
from multiprocessing import Pool


def say_hello(name: str) -> str:
    st_time = time.time()
    print(f'Hi there, {name}')
    en_time = time.time()
    print(f'Completed in {st_time-en_time} second(s)')

def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter = counter + 1
    end = time.time() 
    print(f'Finished counting to {count_to} in {end-start}')
    return counter

if __name__ == '__main__':
    start_time = time.time()
    with Pool() as process_pool:

        to_one_hundred_million = process_pool.apply_async(count, args=(1000000000,))
        to_two_hundred_million = process_pool.apply_async(count, args=(2000000000,))

        hi_jeff = process_pool.apply_async(say_hello, args=('Jeff',))
        hi_mike = process_pool.apply_async(say_hello, args=('Mike',))
        hi_john = process_pool.apply_async(say_hello, args=('John',))

        hi_jeff.get()

        to_one_hundred_million.get()
        to_two_hundred_million.get()

        hi_mike.get()
        hi_john.get()
     
    end_time = time.time()
    print(f'Completed in {end_time-start_time}')

