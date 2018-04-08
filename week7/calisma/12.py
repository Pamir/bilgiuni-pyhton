def faktoriyel(sayi):

    if sayi == 1:
      return 1
    return sayi * faktoriyel(sayi - 1)


if __name__ == "__main__":
    a = faktoriyel(5)
    print(a)