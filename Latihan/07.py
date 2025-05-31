buah= ["pisang", "jambu", "kelapa"]
print("asfa makan:", buah)

buah= ["durian","anggur", "apel", "jeruk", "matoa", "strawberry"]
print("asfa makan buah", buah[3])

hewan= ["ayam", "burung", "bebek", "sapi", "domba"]
hewan[2]= "angsa"
print("asfa punya banyak binatang seperti", hewan)

hewan= ["ayam", "burung", "bebek", "sapi", "domba"]
hewan.append("angsa")
print("asfa punya binatang seperti", hewan)

pohon= []
jumlah=int(input("masukkan jumlah pohon yang kamu tanam: "))
for i in range (jumlah) :
    pohon_user= input(f"masukkan pohon ke-{i + 1}: ")
    pohon.append(pohon_user)
print("jenis pohon yang asfa tanam adalah", pohon)

hewan= ["kucing", "kambing", "koala"]
for peliharaan in hewan :
    print("asfa punya peliharaan", peliharaan)

daur= ["plastik", "organik", "daun"]
i = 0
while i < len(daur) :
    print(f"asfa mendaur ulang {daur[i]}")
    i = i + 1

buah= ["anggur","alpukat", "durian", "jambu"]
for buahan in buah :
    if buahan == "durian" : 
        print(f"asfa makan {buahan}, dan itu buah favorit")
    else :
        print(f"asfa makan {buahan}")

pohon=[]
for i in range(3) :
    pohon_pohon= input(f"masukkan pohon ke {i+1}: ")
    pohon.append(pohon_pohon)
for pepohonan in pohon :
    print(f"asfa menanam pohon {pepohonan}")

makanan_list= ["martabak", "sushi", "bakso"]
i = 0
while i < len(makanan_list):
    if makanan_list [i] == "sushi" :
        print(f"asfa makan {makanan_list[i]}, makanan favorit")
    else :
        print(f"asfa makan {makanan_list[i]}")
    i= i + 1

berat_bayi= []
jumlah= int(input("masukkan jumlah bayi : "))
for i in range(jumlah) :
    berat= float(input(f"masukkan berat bayi ke-{i+1} kg : "))
    berat_bayi.append(berat)
total= 0
for berat in berat_bayi :
    total= total + berat
print(f"total berat seluruh bayi adalah {total} kg")

berat_sampah= [6.7, 8.4, 1.4]
for berat in berat_sampah :
    if berat > 5 :
        print(f" asfa mendaur ulang sampah seberat {berat}, luar biasa")
    else :
        print(f"asfa mendaur ulang sampah seberat {berat}, tambah lagi dong")