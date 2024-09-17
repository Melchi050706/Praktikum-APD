nama = str(input ("masukkan nama anda"))
nim = int(input ("masukkan nim anda"))
harga_setiap_mobil = float(input ("masukkan harga_setiap_mobil"))

modulus = harga_setiap_mobil%7
DiskonTesla = harga_setiap_mobil*0.17
DiskonToyota = harga_setiap_mobil*0.21
DiskonHyundai = harga_setiap_mobil*0.23
hasilAkhirTesla = harga_setiap_mobil-DiskonTesla
hasilAkhirToyota = harga_setiap_mobil-DiskonToyota
hasilAkhirHyundai = harga_setiap_mobil-DiskonHyundai

print("Data Pembeli :", nama, " NIM :", nim)
print ("Mobil Tesla seharga RP.", harga_setiap_mobil, " diskon 17% menjadi Rp.", hasilAkhirTesla, ". Mobil Toyota seharga RP.", harga_setiap_mobil, " diskon 21% menjadi Rp.", hasilAkhirToyota, ". Mobil Hyundai seharga RP.", harga_setiap_mobil, " diskon 23% menjadi Rp.", hasilAkhirHyundai, ". harga setiap mobil modulus 7 adalah ", modulus)
