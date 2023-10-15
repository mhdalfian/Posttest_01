print("Program Menghitung Volume Bangun Ruang")
print(end="\n")

#User melakukan login
nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")
password = input("Masukkan kata sandi: ")

if password == "12345":
        print("Login berhasil!")
        print(end="\n")
else:
        print("Password salah, coba lagi.")
        
        print(end="\n")

#User melakukan input angka yang akan menentukan bangun ruang
print(f"Hai {nama} // {nim}, Pilih bangun ruang:")
print("1. Bola")
print("2. Tabung")
print("3. Limas Segitiga")

#Proses operasi serta menampilkan hasil sesuai input user
pilihan = int(input("Pilih nomor (1/2/3): "))

if pilihan == 1:
    jari2 = float(input("Masukkan jari-jari bola (m): "))
    volume = (4/3) * 3.14 * jari2**3
    print(f"Volume bola adalah {volume:.2f} m3")
elif pilihan == 2:
    jari2 = float(input("Masukkan jari-jari tabung (m): "))
    tinggi = float(input("Masukkan tinggi tabung (m): "))
    volume = 3.14 * jari2**2 * tinggi
    print(f"Volume tabung adalah {volume:.2f} m3")
elif pilihan == 3:
    alas = float(input("Masukkan panjang alas segitiga (m): "))
    tinggi = float(input("Masukkan tinggi segitiga (m): "))
    volume = (1/3) * (alas * tinggi)
    print(f"Volume limas segitiga adalah {volume:.2f} m3")
else:
    print("Pilihan unvalid. Pilih 1, 2, atau 3.")