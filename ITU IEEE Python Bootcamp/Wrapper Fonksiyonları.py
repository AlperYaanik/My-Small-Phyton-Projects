#Wrapper Fonksiyonlarını Test Etmek için verilen ödev
def boslukbırak(func):
  def wrapper(*args):
   print("\n")
   return func(*args)
  return wrapper 


def buyut(func):
  def wrapper(*args):
    x=func(*args)
    return x.upper()
  return wrapper

@boslukbırak
@buyut
def birlestir(txt):
  return txt.replace(" ","")
  
print("String: ")
print(birlestir("Hello World"))