x=int(input("Bir Sayı Giriniz:  "))
y=int(input("İkinci Bir Sayı Giriniz:  "))
Kalan_kontrol = x % y == 0

print(f' x+y = {x+y}\n x-y = {x-y}\n x*y = {x*y}\n x/y = {x/y}\n Bu sayılar birbirine bölünüyor mu?={Kalan_kontrol}')