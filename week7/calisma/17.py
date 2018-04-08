def add(a, b):
    print("{0} {1}".format(a, b))
    return a + b


if __name__ == "__main__":
    c = add
    print(c)
    print(c(12, 13))
