akuns = []
pembelian_tiket = []

while True:
    print("Halo! selamat datang di list pembelian tiket bus")
    print("Silakan pilih 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
    print("1. Daftar akun")
    print("2. Login")
    print("3. Exit")
    print("――――――――――――――――――――――――")
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        print("Halo Pengguna baru! Ayo buat akun dulu")
        Username = input("Username: ")
        akuna = False
        for akun in akuns:
            if akun[0] == Username:  # Memeriksa apakah username sudah ada
                akuna = True
                break
        if akuna:
            print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
        else:
            Password = input("Password: ")
            akuns.append([Username, Password, []])  # Simpan username, password, dan catatan (sebagai list kosong)
            print(f"Akun Anda berhasil terdaftar dengan ID: {Username}")
 

    elif opsi == "2":
        print("Hi, Silahkan login dulu ya!")
        Username = input("Username: ")
        Password = input("Password: ")
        for akun in akuns:
            if akun[0] == Username and akun[1] == Password:  # Cocokkan username dan password
                while True:
            
                    print(f"\nSelamat datang {Username}!")
                    print("―――Silakan pilih menu!―――")
                    print("1. Tambah Tiket")
                    print("2. Lihat Semua Tiket")
                    print("3. Ubah Tiket")
                    print("4. Hapus Tiket")
                    print("5. Keluar")
                    print("__________________")

                    pilihan = input("Pilih menu (1-5): ")
                    if pilihan == "1":
                
                        nama = input("Masukkan nama penumpang: ")
                        tujuan = input("Masukkan tujuan: ")
                        harga = input("Masukkan harga: ")
                        pembelian_tiket.append([nama, tujuan, harga])
                        print("Tiket berhasil ditambahkan!\n")

                    elif pilihan == "2":
                        if pembelian_tiket:
                            for index, tiket in enumerate(pembelian_tiket, start=1):
                                print(f"{index}. Nama: {tiket[0]}, Tujuan: {tiket[1]}, Harga: {tiket[2]}")
                        else:
                            print("Belum ada pembelian tiket.\n")
                        input("klik enter untuk lanjut...")

                    elif pilihan == "3":
                        for index, tiket in enumerate(pembelian_tiket, start=1):
                            print(f"{index}. Nama: {tiket[0]}, Tujuan: {tiket[1]}, Harga: {tiket[2]}")
                            print()                        
                        ubah = int(input("Masukkan nomor tiket yang ingin diubah: ")) - 1
                        if 0 <= ubah < len(pembelian_tiket):
                            nama_baru = input("Masukkan nama penumpang baru: ")
                            tujuan_baru = input("Masukkan tujuan baru: ")
                            harga_baru = input("Masukkan harga baru: ")
                            pembelian_tiket[ubah] = [nama_baru, tujuan_baru, harga_baru]
                            print("Tiket berhasil diubah!\n")

                    elif pilihan == "4":
                        for index, tiket in enumerate(pembelian_tiket, start=1):
                            print(f"{index}. Nama: {tiket[0]}, Tujuan: {tiket[1]}, Harga: {tiket[2]}")
                            print()
                        hapus = int(input("Masukkan nomor tiket yang ingin dihapus: ")) - 1
                        if 0 <= hapus < len(pembelian_tiket):
                            del pembelian_tiket[hapus]
                            print("Tiket berhasil dihapus!\n")
                        else:
                            print("Tidak ada tiket yang kamu maksud, silakan input ulang.\n")

                    elif pilihan == "5":
                        print("Terima kasih Karena Sudah Mau Ngelist!")
                        print()
                        break
                    
                    else:
                        print("Pilihan tidak ada, silahkan input ulang.\n")
                break
    elif opsi == "3":
        print("Apakah kamu yakin ingin keluar? ")
        print("1. Iya")
        print("2. Tidak")
        pilih = input("Input pilihan: ")
        print(" ")
        if pilih == "1":
            print("Terimakasih sudah mau melihat list pembelian tiket bus, semoga harimu menyenangkan!")
            break
        elif pilih == "2":
            continue
        else:
            print("Input tidak valid, silahkan pilih '1' atau '2'\n")
    else:
        print("Input tidak valid, silahkan pilih 1, 2, atau 3")    