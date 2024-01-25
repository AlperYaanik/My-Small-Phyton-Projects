ilanlar,özellikler={},{}
ilan_ad=""
while True:
  print("-----------------\n İlan Eklemek: 1\n İlan Çıkarmak: 2\n Çıkış: 3\n-----------------")
  loop=int(input(" Yapmak İstediğiniz İşlemi Seçin: "))
  if loop==1:
    ilan_giris=input("İlan Adı Giriniz: ")
    if(ilan_giris==ilan_ad):
      print("Bu adlı ilan zaten var")
      continue
    else:
        ilan_ad=ilan_giris
        araba_model=input("Araba Modeli Giriniz: ")
        araba_yıl=int(input("Araba Yılını Giriniz: "))
        araba_fiyat=float(input("Araba Fiyatını Giriniz: "))
        özellikler= {
            'İlan Adı':ilan_ad,
            'Araba Modeli': araba_model,
            'Araba Yılı': araba_yıl,
            'Araba Fiyatı': araba_fiyat
        }

  elif(loop==2):
    ilan_giris=input("Çıkaracağınız ilan adı seçiniz: ")
    if(ilan_giris!=ilan_ad):
      print("Böyle Bir İlan Yok")
    else:
      özellikler= {
          'İlan Adı':"",
          'Araba Modeli': "",
          'Araba Yılı': 0,
          'Araba Fiyatı': 0
      }
  elif(loop==3):
   print("Hatalı İşlem Numarası!")
  else:
   print("Çıkılıyor...")
   break
  ilanlar[özellikler['İlan Adı']]={
    'Araba Modeli':özellikler['Araba Modeli'],
    'Araba Yılı':özellikler['Araba Yılı'],
    'Araba Fiyatı':özellikler['Araba Fiyatı']
  }

    
    