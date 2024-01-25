class Account():
  def __init__(self, account_holder, balance=0):
    self.accountholder = account_holder
    self.balance = balance
    
  def deposit(self,amount):
    self.balance += amount
    return f'{amount} Değeri Eklenince Yeni Bakiye: {self.balance}'
  
  def withdraw(self,amount):
    try:
      if self.balance - amount < 0:
          raise ValueError("Bakiyeniz yetersiz")
        
      else:
          self.balance -= amount
          return f'{amount} Değeri Çekilince Yeni Bakiye: {self.balance}'
    except ValueError as e:  
      print(f'Hata: {e}')
    return f' '

class SavingAccount(Account):
  def __init__(self,accountholder,interest_rate,balance=0):
    super().__init__(accountholder,balance)
    self.interest_rate = interest_rate

  def add_interest(self):
    faiz_geliri=self.balance*self.interest_rate
    return faiz_geliri
    
class CheckingAccount(Account):
  def __init__(self,accountholder,overdraft_limit,balance=0):
    super().__init__(accountholder,balance)
    self.overdraft_limit = overdraft_limit
    
  def withdraw(self,amount):
    try:
      if amount>self.balance+self.overdraft_limit:
          raise ValueError("Borç Oranınız Yetersiz")
      else:
        self.balance -= amount
        return f'{amount} Değeri Çekilince Yeni Bakiye: {self.balance}'
    except ValueError as e:
      print(f'Hata: {e}')
    return f' '


hesap = Account("Mustafa Sandal", balance=1000)
print(hesap.deposit(500))
print(hesap.withdraw(200))
print(hesap.withdraw(3000))

saving_account = SavingAccount("Mustafa Sandal", interest_rate=0.05,balance=300)
print(f'Faiz Oranı: %{saving_account.add_interest()}')

checking_account = CheckingAccount("Musatafa Sandal", overdraft_limit=500, balance=100)
print(checking_account.withdraw(150))
print(checking_account.withdraw(750))