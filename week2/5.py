a = ["o","s","m","a","n","a"]
b = len(a)
ort = b / 2
tekmi = True
if b % 2 ==0:
    tekmi = False

if tekmi == True :
    ort = int(round(ort))
ort2 =  int(ort)
for i in range (0,ort2):
    tmp = a[i]
    a[i] = a[0 -(i+1)]
    a[0 -(i+1)] = tmp
print(a)