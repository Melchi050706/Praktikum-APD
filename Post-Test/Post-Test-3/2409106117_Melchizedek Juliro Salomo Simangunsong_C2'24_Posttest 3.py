mobil = str(input ("Bu Navira Ingin membeli mobil bermerek 1. tesla 2. toyota 3. hyundai "))

if mobil == "1" or mobil == "2" or mobil == "3" :
    harga_mobil = int(input ("masukkan harga mobil "))
    if mobil == "1" :
        tesla_diskon = harga_mobil*0.17
        tesla = harga_mobil-tesla_diskon
        print ("potongan harga tesla =", tesla_diskon, "harga tesla yang dibayar = ", tesla)

    elif mobil == "2" :
        toyota_diskon = harga_mobil*0.21
        toyota = harga_mobil-toyota_diskon
        print ("potongan harga toyota =", toyota_diskon, "harga toyota yang dibayar = ", toyota)

    elif mobil == "3" :
        hyundai_diskon = harga_mobil*0.23
        hyundai = harga_mobil-hyundai_diskon
        print ("potongan harga hyundai =", hyundai_diskon, "harga hyundai yang dibayar = ", hyundai)

else :
    print ("Jika Tidak membeli apa², Maka Bu Navira tidak jadi membeli mobil")
