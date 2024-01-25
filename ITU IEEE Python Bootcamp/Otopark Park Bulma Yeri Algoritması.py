
def otopark_olustur(n):
  otopark = [[0] * n for _ in range(n)]
  return otopark

#Otoparkın Çizilmesi
def otopark_ciz(otopark):
  result = ""
  for i in otopark:
    result += str(i) + "\n"
  return result.strip()

#Boş Yeri Bulma Algoritması
def yer_bul(otopark):
  size=len(otopark)-1
  x=0
  y=2*size
  while y>=0:
    for k in range(x,-1,-1):
      i,j=size,size
      i-=k
      j=y-i
      if otopark[i][j]==0:
        return i,j  
      
    x+=1    
    y-=1
    
  return None,None





def arac_ekle(otopark, n):

  i, j = yer_bul(otopark)
  otopark[i][j] = 1
  if n > 1:
    return arac_ekle(otopark, n - 1)
  else:
    pass


def main():
  n = int(input("Otoparkın Bir Kenar Uzunluğu: "))
  otopark = otopark_olustur(n)
  print(f"Otopark:\n{otopark_ciz(otopark)}")
  while True:
    try:

      cevap = int(input("Eklenecek Araç Sayısı Girin:"))

      arac_ekle(otopark, cevap)
      print(f"Otopark:\n{otopark_ciz(otopark)}")
    except ValueError:
      print("Geçerli bir değer girilmedi! İşlem iptal ediliyor..")
      break
    except:
      print("Hata! İşlem iptal ediliyor...")
      break


main()
