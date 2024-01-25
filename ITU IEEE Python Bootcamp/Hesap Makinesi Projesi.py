def calculator():
  #Kullanıcı Girişi Alma
  def get_user_input():
    x=float(input("İlk Sayı: "))
    y=float(input("İkinci Sayı: "))
    return x,y
#Toplama
  def add(x, y):
    return x+y
#Bölme
  def divide(x,y):
     try:
        return x/y
     except ZeroDivisionError:
        print("Sıfıra bölme hatası")
        pass 
       
   
#Çarpma
  def multiply(x,y):
    return x*y
#Çıkarma
  def subtract(x,y):
    return x-y

  select=0
  while(select!=5):
    
    select=input("İşlem Seçin:\n1. Toplama (+)\n2. Çıkarma (-)\n3. Çarpma (*)\n4. Bölme (/)\n5. Çıkış\nİşlem Seçiniz: ")
    if not select.isnumeric():
      print("\nGiriş String Olamaz")
      print("\n")
      continue
    elif float(select)!= int(select):
      print("\nGiriş Float Olamaz")
      print("\n")
      continue
    else:
      select=int(select)
    #Çıktılar Yazılıyor
      if select==5:
        print("Çıkış Yapılıyor")
        break
      elif select==1:
         x,y=get_user_input() 
         print(f'{x} + {y} = {add(x,y)}')
      elif select==2:
         x,y=get_user_input() 
         print(f'{x} - {y} = {subtract(x,y)}')  
      elif select==3:
         x,y=get_user_input() 
         print(f'{x} * {y} = {multiply(x,y)}')  
      elif select==4:
         x,y=get_user_input()
         #if y==0:
            #print("0'a bölme işlemi yapılamaz")
            #continue
         print(f'{x} / {y} = {divide(x,y)}')
      else:
         print("Hatalı İşlem Yaptınız")   
        
      print("\n")
  pass

calculator()
  