import time
import asyncio


def is_prime(x):
    """
    You must include a 0.01 sleep in this method for the purpose of the async test
    """
    time.sleep(0.01)
    return not any(x // i == x / i for i in range(x - 1, 1, -1))


def highest_prime_below(x):
    
    """
    ToDo
    Create a function to find the highest prime number below the input x.
    You have to use is_prime to check if a number is prime or not
    """
    max_prime = 0

    for i in range(x):
        if is_prime(i):
            max_prime = i

    return max_prime



def main():
    t0 = time.time()

    highest_prime_below(100000),
    highest_prime_below(10000),
    highest_prime_below(1000)

    t1 = time.time()
    print('Took %.2f ms' % (1000 * (t1 - t0)))


main()

"""
Part 1.  Create the highest_prime-below method
Part 2. use asyncio to make main run faster
"""