şifre=""
alfabe="abcçdefgğhıijklnmoöprsştuüvyz"
#Yaparken n ile m nin yerini sizin örneğinize uysun diye değiştirdim 

##Alfabe sırasına göre bir sonraki harf ile değiştirerek şifreleme yapmak
print("------------\n1-Şifreleme\n2-Şifre Çözme\n------------")
işlem=int(input("İşlem Seçiniz: "))

if(işlem==1):
  
  metin=input("Metin Giriniz: ").lower()
  for harf in metin:
    
    if harf in alfabe:
      şifre+=alfabe[(alfabe.index(harf)+1)]
       
    else:
      print("Lütfen Türkçe Karekter Giriniz")
      break
  print("Şifrelenmiş metin: {}".format(şifre))


#Alfabe sırasına göre bir önceki harf ile değiştirerek şifreyi kırmak
elif(işlem==2):
   metin=input("Metin Giriniz: ").lower()
   for harf in metin:

     if harf in alfabe:
       şifre+=alfabe[alfabe.index(harf)-1]

     else:
       print("Lütfen Türkçe Karakter Giriniz")
       break
   print("Şifresi Çözülmüş Metin: {}".format(şifre))
else:
  print("Hatalı işlem!")