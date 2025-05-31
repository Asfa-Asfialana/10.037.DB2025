pohon_dic= {"kelapa": 5, "sawit": 10, "pinang": 25}
print(f"asfa punya kebun {pohon_dic}")
print(f"kebun sawit asfa sebanyak {pohon_dic['sawit']}")
pohon_dic['sawit']=20
print(f"asfa punya kebun{pohon_dic}")
pohon_dic ['kopi']=15
print(f"asfa mempunyai kebun {pohon_dic}")

pohon_dictionary= {}
jumlah= int(input("masukkan jumlah pohon: "))
for i in range(jumlah) :
    pohon= input(f"masukkan jenis pohon ke-{i+1}: ")
    jumlah_pohon= int(input(f"masukkan jumlah {pohon}: "))
    pohon_dictionary[pohon]=jumlah_pohon
print(f"asfa menanam {pohon_dictionary}")

for pohon, jumlah in pohon_dic.items() :
    print(f"asfa menanam {pohon} : {jumlah}")

keys= list(pohon_dic.keys())
i = 0
while i < len(keys) :
    pohon= keys[i]
    print(f"asfa menanam {pohon} : {pohon_dic[pohon]}")
    i= i + 1

for pohon, jumlah in pohon_dic.items() :
    if jumlah > 10 :
        print(f"asfa menanam {pohon} : {jumlah}, wah hebat sekali!")
    else :
        print(f"asfa menanam {pohon} : {jumlah}, tambah lagi ya!")

keys= list(pohon_dic.keys())
i=0
while i < len(keys) :
    pohon= keys[i]
    jumlah= pohon_dic[pohon]
    if jumlah >20 : 
        print(f"asfa menanam {pohon} pohon : {jumlah}, wah banyak!")
    else : 
        print(f"asfa menanam {pohon} pohon : {jumlah},tingkatkan")
    i= i+1

pohon_dict= {}
for i in range (3) :
    pohon1= input(f"masukkan nama pohon ke-{i + 1} : ")
    jumlah1= int(input(f"masukkan jumlah {pohon1} pohon : "))
    pohon_dict[pohon1]=jumlah1
for pohon1, jumlah1 in pohon_dict.items() :
    print(f"asfa menanam {pohon1} : {jumlah1}")

sampah_dict= {}
jumlah_sampah= int(input('masukkan jumlah sampah anda : '))
for i in range(jumlah_sampah) :
    jenis= input(f"masukkan jenis sampah ke{i+1} :  ")
    berat= float(input(f"masukkan berat sampah {jenis} :   "))
    sampah_dict[jenis]=berat
total=0
for berat in sampah_dict.values() :
    total= total+berat
print(f"asfa mendaur semua jenis sampah seberat {total} kg")

kopi={}
i=0
while i < 2 :
    jenis_kopi= input(f"masukkan jenis biji kopi ke{i+1}: ")
    berat_kopi=float(input(f"masukkan berat kopi {jenis_kopi} kg :  "))
    kopi[jenis_kopi]=berat_kopi
    i= i+1
total_kopi=0
for jenis_kopi, berat_kopi in kopi.items():
    total_kopi= total_kopi+berat_kopi
    if total_kopi > 15 :
        print(f"asfa membeli biji kopi {total_kopi}, wah banyak!")
    else :
        print(f"asfa membeli biji kopi {total_kopi}, tambah lagi!")