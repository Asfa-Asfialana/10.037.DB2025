jumlah_pohon= int(input("berapa jumlah pohon yang kamu tanam selama ini : "))
if jumlah_pohon > 30 : print("Kamu sudah menanam banyak pohon. \n sangat keren, dan lanjutkan!")
else : print("kamu perlu tanam lebih banyak pohon. \n semangat ya!")

berat_sampah= float(input("berapa berat sampah yang kamu daur ulang hari ini:  "))
if berat_sampah > 15 : print("Selamat, kamu sudah mendaur ulang banyak sampah hari ini")
else : print ("oops, kamu harus daur ulang lebih banyak sampah hari ini. silahkan coba lagi \n semangat ya!")

hemat_energi= True
if hemat_energi : print("asfa sudah hemat energi, hebat sekali!")
else : print("asfa tidak hemat energi!")

daur_sampah= False
if daur_sampah: print ("kamu mendaur ulang sampah dengan baik")
else : print ("kamu perlu mendaur ulang sampah dengan baik")

donasi= int(input("berapa jumlah donasi yang akan anda berikan : "))
penerima= int(input("berapa jumlah penerima : "))
sisa_donasi= donasi % penerima
if sisa_donasi == 0 : print("donasi dibagi rata")
else : print(f" sisa penerima adalah {sisa_donasi} ")

tong_daur_ulang= int(input(" berapa jumlah tong :  "))
rumah_warga= int(input("berapa jumlah rumah yang akan diberikan tong: "))
pembagian= tong_daur_ulang // rumah_warga
if pembagian > 3 : print (f" jumlah tong yang dibagikan {pembagian} \n tong daur ulang sampah dibagikan secara merata")
else : print(f"jumlah yang dibagikan sebanyak {pembagian} \n pembagian tong daur ulang sampah tidak merata")

sampah= float(input("masukkan berat awal sampah anda: "))
daur= float(input(" masukkan berat sampah yang sudah anda daur ulang : "))
tambah= float(input(" masukkan berat sampah tambahan: "))
hasil_akhir= (sampah - daur + tambah) * 7 / 3
if hasil_akhir > 50:
    print(f"Arry Hutomo hitung sampah {hasil_akhir} kg!\nLuar biasa ", "bareng ECC Team!", sep="=>", end="")
    print("yuk!")
else:
    print(f"Arry Hutomo hitung sampah {hasil_akhir} kg!\nTambah lagi ", "bareng ECC Team!", sep="=>", end="")
    print("yuk!")