class Banka:
  def __init__(self):
    self.anapara=0 #Ana Para
    self.faiz_oran=0 #Yıllık Faiz Oranı
    self.vade=0 #Vade
    self.total=round((((self.faiz_oran/12)*    
    (self.vade))/100)*self.anapara,5) #Faiz Getirisi

  def set_para(self,para):
    self.anapara=float(para) 
    
  def set_faiz(self,faiz):
    self.faiz_oran=float(faiz)
    
  def set_vade(self,vade):
    self.vade=int(vade)

  def get_total(self):
    self.total=round((self.faiz_oran/12*    
    self.vade/100*self.anapara),3)
    return self.total

#Bilgilerin Alınma Kısmı
baslangıc_para=input("Lütfen Ana Para Değerinizi Giriniz: ")
baslangıc_vade=input("Lütfen Vadenizi Ay Sayısı Olarak Giriniz: ")
baslangıc_faiz=input("Lütfen Yıllık Faiz Oranınızı Giriniz: ")
#Bilgilerin Class'a işlenmesi
kullanıcı=Banka()
kullanıcı.set_para(baslangıc_para)
kullanıcı.set_faiz(baslangıc_faiz)
kullanıcı.set_vade(baslangıc_vade)
#Ekrana Yazdırma
print(f'{baslangıc_vade} ay sonunda, yıllık %{baslangıc_faiz} faiz oranı ile {baslangıc_para}TL ana paradan {kullanıcı.get_total()}TL faiz geliri elde edilecektir.')
