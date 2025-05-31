jumlah_pohon= 20
print(f"hari ini aku menanam {jumlah_pohon} pohon!")

berat_sampah= 15.2
print(f"asfa mendaur ulang sampah seberat {berat_sampah}!")
hemat_energi= True
print(f"asfa bilang: hemat energi itu {hemat_energi}!")

jumlah=20
barang= "pohon"
nama= "arry utomo"
print(f"asfa menanam {jumlah} {barang}", f"bareng {nama}! \n Ayo ikut ", sep="=>", end="")
print("sekarang")



pohon_dict = {}
for i in range(3):
    pohon = input(f"Masukkan nama pohon ke-{i+1}: ")
    jumlah = int(input(f"Masukkan jumlah {pohon}: "))
    pohon_dict[pohon] = jumlah
for pohon, jumlah in pohon_dict.items():
    print(f"Arry Hutomo tanam {pohon}: {jumlah}!")