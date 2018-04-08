def validate_tck(tckn):

    a = tckn

    if kontrol(tckn) == False:
        return False

    total = 0

    for i in range(0,10):
        total = total + int(a[i])
        print(a[i])

    sonuc = total % 10 == int(a[10])

    print(total)
    print(sonuc)

    return sonuc

def kontrol(tckn):
    return len(tckn) == 11


if __name__ == "__main__":

    while True:
        tckn = input(" Yaz : ")
        val = validate_tck(tckn)
        if val == True:
            print("TCKN doğru")
            break
        else:
            print("TCKN yanlış password")



