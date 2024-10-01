username = "melchi"
password = "117"
gagal = 0

print(f"Anda memiliki 3 kali kesempatan untuk login")
while gagal <3:
  
  login_user = input("masukkan username anda : ")
  login_password = (input("masukkan password anda: "))
  
  if login_user == username and login_password == password:
    print("login berhasil")

    print("Mau membeli mobil bermerek apa?\n 1. tesla\n 2. toyota\n 3. hyundai")
    mobil = str(input("Pilihan anda: "))
    

    if mobil == "1" :
        harga_mobil = int(input ("Masukkan harga mobil: "))
        tesla_diskon = harga_mobil*0.17
        tesla = harga_mobil-tesla_diskon
        print ("potongan harga tesla =", tesla_diskon, "harga tesla yang dibayar = ", tesla)

    elif mobil == "2" :
        harga_mobil = int(input ("Masukkan harga mobil: "))
        toyota_diskon = harga_mobil*0.21
        toyota = harga_mobil-toyota_diskon
        print ("potongan harga toyota =", toyota_diskon, "harga toyota yang dibayar = ", toyota)

    elif mobil == "3" :
        harga_mobil = int(input ("Masukkan harga mobil: "))
        hyundai_diskon = harga_mobil*0.23
        hyundai = harga_mobil-hyundai_diskon
        print ("potongan harga hyundai =", hyundai_diskon, "harga hyundai yang dibayar = ", hyundai)

    else :
        print ("Jika Tidak membeli apa², mending pulang")
        exit()

    break

  else:
      gagal += 1
      print(f"anda telah gagal sebanyak {gagal}x")
if gagal == 3:
      print(f"percobaan login anda gagal, anda di banned selamanya")
      print()

      