jumlah_pohon= int(input("masukkan jumlah pohon yang kamu tanam:    "))
print(f"terimakasih, kamu menanam pohon sebanyak {jumlah_pohon} hari ini!")

jumlah_sampah=float(input("berapa berat sampah yang kamu daur ulang hari ini:    "))
print(f"kamu mendaur ulang sampah seberat {jumlah_sampah} kg hari ini!")

nama_komunitas= input("masukkan nama komunitas anda disini:   ")
print(f"Asfa bersama {nama_komunitas} menanam pohon bersama!")

jumlah_pohon_sebelumnya= int(input("masukkan jumlah pohon yang anda tanam sebelumnya:   "))
jumlah_tambahan= int(input("masukkan pohon tambahan yang anda tanam hari ini:   "))
print(f"total pohon yang anda tanam saat ini : {jumlah_pohon_sebelumnya + jumlah_tambahan}")

pohon=int(input("masukan jumlah pohon saat ini:   "))
tambah=int(input("masukan jumlah pohon tambahan:  "))
mati=int(input("masukan jumlah pohon yang mati saat ini:    "))
total= (pohon + tambah - mati) /2
print(f"Total pohon anda saat ini adalah {total} !")

donasi= int(input("berapa jumlah donasi yang ingin kamu berikan : Rp. "))
print(f"kamu memberikan donasi sebesar {donasi} kepada UMKM.\n Terima kasih!")

lampu= int(input("berapa jumlah lampu satu ruangan: "))
jumlah_ruangan= int(input(" berapa jumlah ruangan: "))
total_lampu= lampu * jumlah_ruangan
print(f"jumlah lampu yang dibutuhukan satu gedung ini adalah sebanyak {total_lampu} lampu ")