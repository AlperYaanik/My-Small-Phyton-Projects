note=[]
note.append(input("Adınızı Giriniz: "))
note.append(input("Soyadınızı Giriniz: "))
note.append(input("CRN Giriniz: "))
note.append(input("Ders Adı Giriniz: "))
note.append(input("Birinci Vize Giriniz: "))
note.append(input("İkinci Vize Giriniz: "))
note.append(input("Final Giriniz: "))
ortalama= 0.3*int(note[4])+0.3*int(note[5])+0.4*int(note[6])
print(f' Adı:{note[0]} \n Soyadı:{note[1]} \n CRN:{note[2]} \n Ders Adı:{note[3]}')
print(f' Birinci Vize:{note[4]} \n İkinci Vize:{note[5]} \n Final:{note[6]}')
print(f' Okulumuz öğrencilerinden {note[0]},{note[2]}-{note[3]} dersinden {round(ortalama,4)} ortalamaya sahiptir.')