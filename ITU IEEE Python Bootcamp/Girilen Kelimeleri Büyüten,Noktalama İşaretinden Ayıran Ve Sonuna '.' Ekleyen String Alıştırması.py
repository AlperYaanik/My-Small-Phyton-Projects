def string_combiner(*args):
  
  try:
    noktalama = ('.', ',', '!', '?')
    string_args = ""
#Noktalama işareti içeriyor mu diye bakıyoruz
    for harf in args:
      if not isinstance(harf, str):
        raise TypeError
      for char in harf:
       
        if char not in noktalama:
       
          string_args += char
    
      string_args += " "

    string_args=string_args[:-1]
    nokta =string_args[-1]
#Sonunda nokta yoksa nokta ekliyoruz
    if  nokta != '.':
      string_args+="."
  
    return string_args
  except TypeError:
    return "String Giriniz"


print(string_combiner("I.", "E","!E","E"))
