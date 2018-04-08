a = input("Kredi kartı numaranızı yazınız : ")

total = 0

if len(a) != 16:
    exit(-1)

for i in range(0,16):
    if i % 2 == 0:
        total = total + int(a[i])
    else:
        total = total + int(a[i]) * 2

sonuc = total % 10 == 0

if sonuc:
    print("Kredi kartı geçerlidir")
else:
    print("Hatalı giriş")