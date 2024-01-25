###Dictionary Oluşturma
country_dict = {
  "Türkiye" : "Ankara",
  "Rusya"   : "Moskova",
  "Azerbaycan" : "Baku",
}
###Boş liste
country_list = []
###Listeye Dictionaryi ekleme
for country,capital in country_dict.items():
  country_list.append(country)
  country_list.append(capital)
  ### Listenin uzunluğunu döngülerle bulma
lenght=0
for i in country_list:
    lenght+=1
### Listeyi Tersten Yazdırma
for list in range(-1,-lenght-1,-1):
  print(country_list[list])