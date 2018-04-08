def fib(p):
    if p == 0 or p == 1:
        return 1
    return fib(p-1) + fib(p-2)
if __name__ == "__main__":

    print(fib(5))