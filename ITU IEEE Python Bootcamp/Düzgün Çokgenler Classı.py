class Sekil:
  def __init__(self,kenar_sayısı):
    self.kenar_sayısı=kenar_sayısı
  
  def iç_açılar_toplamı(self):
    ic_acı_toplam=(self.kenar_sayısı-2)*180
    return ic_acı_toplam
   
  def bir_ic_acı(self):
    ic_acı_toplam=self.iç_açılar_toplamı()
    bir_ic_acı=ic_acı_toplam/self.kenar_sayısı
    return bir_ic_acı

kare=Sekil(4)
print(f"Kare'nin İç Açılar Toplamı:{kare.iç_açılar_toplamı()}")
print(f"Düzgün Kare'nin Bir İç Açısı:{kare.bir_ic_acı()}")