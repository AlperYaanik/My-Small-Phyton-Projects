class Product:
  def __init__(self, name, price, stock_quantity):
    self.name = name
    self.price = price
    self.stock_quantity=stock_quantity

#İndirim Fonksiyonu
  def apply_discount(self, discount_percentage):
    price_with_discount=self.price*(1-discount_percentage/100)
    return  price_with_discount
#Bilgileri Gösteren Fonksiyon    
  def display_info(self):
    print(f"\nProduct: {self.name}")
    print(f"Price: {self.price}")
    print(f"Stock Quantity: {self.stock_quantity}\n")

class Costumer(Product):
  def __init__(self,name,mail):
    self.name=name
    self.mail=mail
    self.shopping_cart=ShoppingCart()
#Karta Ürün Ekleme
  def add_to_card(self,product,quantity):
    self.shopping_cart.add_item(product,quantity)
#Sipariş Verme
  def place_order(self):
    self.shopping_cart.display_cart()
    print(f"Toplam Tutar:{self.shopping_cart.calculate_total()}")



class ShoppingCart(Product):
  def __init__(self):
    self.items=[]
#Ürünü Eklemenin Lojiği
  def add_item(self,product,quantity):
    if product.stock_quantity >quantity:
      is_exist_product=None
      for item in self.items: 
        if item["product"].name == product.name:
          is_exist_product=item
          break
        
      if is_exist_product:
         is_exist_product["quantity"]+=quantity
      else:  
         item={"product":product,"quantity":quantity}
         self.items.append(item)
        
      product.stock_quantity -= quantity
      
    else:
      print(f"Ürün Stoğumuz Yetersizdir\nMevcut Ürün Stoğu: {product.stock_quantity}")
  #Sipariş Sepetini Göstermek
  def display_cart(self):
    for item in self.items:
       product=item["product"]
       quantity=item["quantity"]
       print(f"{product.name} adlı {product.price} değerindeki ürün {quantity} adet alındı.")
#Ürün Fiyatlarını Hesaplama
  def calculate_total(self):
    total_price=0
    for item in self.items:
       product=item["product"]
       quantity=item["quantity"]
       total_price+=product.price*quantity
    return total_price





product1 = Product("Laptop", 1200, 10)
print(f"%15 indirimli fiyatı: {product1.apply_discount(15)}")
product1.display_info()

customer1 =Costumer("Serdar","örnekeposta1@gmail.com")
customer1.add_to_card(product1, 3)

product2=Product("Mouse",100,4)
customer1.add_to_card(product2, 3)
customer1.add_to_card(product1, 3)
customer1.place_order()

product1.display_info()
customer2 =Costumer("Şafak ", "örnekeposta2@gmail.com")
customer2.add_to_card(product2, 3)
customer2.place_order()

###Her Kullanıcı Bir Kere sipariş verebiliyor açıklamada belirtilmediği için sepetteki ürünleri yeni class açıp yapılan siparişlerin içine atmadım###