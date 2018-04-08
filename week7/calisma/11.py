def faktoriyel(sayi):
    sonuc = 1
    for i in range(1,sayi+1):
        sonuc = sonuc * i
    return sonuc


if __name__ == "__main__":
    a = faktoriyel(5)
    print(a)

