#Birinci soru başlangıç
import random

arr = [None] * 100
for i in range(1, 100):
    arr[i] = i

arr[0] = random.randint(1, 99)
print(arr)
random.shuffle(arr)
