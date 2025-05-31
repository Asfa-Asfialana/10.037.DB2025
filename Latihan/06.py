for i in range (5) :
    print("asfa menanam pohon")

count = 0
while count < 3 :
    print ("asfa menanam pisang")
    count = count + 1

for i in range (1, 5):
    print(f"asfa membeli {i} buku")

pohon= 1
while pohon <= 8 :
    print(f"asfa menyulam {pohon} pohon")
    pohon = pohon + 1

jumlah= int(input("masukkan jumlah buku yang kamu donasikan : "))
for i in range (jumlah):
    print("saya mendonasikan buku")

sampah= float(input("berat sampah anda : "))
berat= 0
while berat<sampah :
    print("saya mendaur ulang sampah")
    berat=berat + 1

total_pohon= 0
for i in range(1, 7) :
    total_pohon= total_pohon + i
    print(f"asfa membeli {total_pohon} pohon")

donasi= 20000
while donasi < 50000:
    donasi= donasi + 10000
    print(f"asfa memberi {donasi} donasi ke umkm")


for i in range(5):
    if i % 2 == 0:
        print(f"Arry Hutomo tanam pohon ke-{i}, genap!")
    else:
        print(f"Arry Hutomo tanam pohon ke-{i}, ganjil!")

hemat_energi= 0
while hemat_energi < 7 :
    hemat_energi= hemat_energi + 1
    if hemat_energi >2 :
        print(f"asfa hemat energi {hemat_energi}")
    else : 
        print(f"asfa tidak hemat energi {hemat_energi}")

pohon= int(input("berapa jumlah pohon yang kamu tanam: "))
jumlah= 0
for i in range(pohon) :
    jumlah=jumlah + 2
    print(f"asfa menanam {jumlah} pohon")

donasi= int(input("masukkan jumlah donasi anda: "))
total=0
while total < donasi:
    total= total + 2000
    print(f"asfa donasi sebanyak {total}")

for i in range(3) :
    if i % 2 == 0 :
        print(f"asfa nanam pohon ke-{i}, genap")
    else :
        print(f"asfa nanam pohon ke{i}, ganjil")

donasi=int(input("masukkan donasi anda: "))
target= 0
while target < donasi :
    target= target + 1000
    if target > donasi:
        print(f"kamu donasi sebesar {target} \n Target tercapai")
    else : 
        print(f"kamu donasi sebesar {target}, \n Target tidak tercapai")

jumlah=int(input("masukkan jumlah pohon yang kamu tanam:  "))
pohon=0
for i in range (jumlah) :
    pohon= pohon + 1
    if pohon > 3 :
        print(f"asfa menanam pohon ke{pohon}, \n bersama","tim ETL",sep= " => ", end=" ")
        print("wah, hebat!")
    else :
        print(f"asfa menanam pohon sebanyak {pohon}, \n bersama", "tim ETL", sep=" => ", end=" ")
        print("tambah lagi!")

    