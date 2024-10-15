akuns = {}

while True:
    print("Halo! Selamat datang di list pembelian tiket bus")
    print("Silakan pilih 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
    print("1. Daftar akun")
    print("2. Login")
    print("3. Exit")
    print("――――――――――――――――――――――――")
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        print("Halo Pengguna baru! Ayo buat akun dulu")
        username = input("Username: ")
        if username in akuns:
            print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
        else:
            password = input("Password: ")
            akuns[username] = {"password": password, "tiket": {}}  
            print(f"Akun Anda berhasil terdaftar dengan ID: {username}")

    elif opsi == "2":
        print("Hi, Silahkan login dulu ya!")
        username = input("Username: ")
        password = input("Password: ")
        if username in akuns and akuns[username]["password"] == password:  
            while True:
                print(f"\nSelamat datang {username}!")
                print("\n=== Menu Pembelian Tiket Bus ===")
                print("1. Tambah Tiket")
                print("2. Lihat Tiket")
                print("3. Update Tiket")
                print("4. Hapus Tiket")
                print("5. Keluar")
                print("_____________________")
                pilihan = input("Pilih menu: ")

                if pilihan == "1":
                    id_tiket = input("Masukkan ID Tiket: ")
                    nama_penumpang = input("Masukkan Nama Penumpang: ")
                    tujuan = input("Masukkan Tujuan: ")
                    harga_tiket = input("Masukkan Harga Tiket: ")
                    akuns[username]["tiket"][id_tiket] = {
                        "Nama Penumpang": nama_penumpang,
                        "Tujuan": tujuan,
                        "Harga Tiket": harga_tiket
                    }
                    print(f"Tiket dengan ID {id_tiket} berhasil ditambahkan.")

                elif pilihan == "2":
                    tiket = akuns[username]["tiket"]
                    if tiket:
                        for id_tiket, lihat in tiket.items():
                            print(f"\nID Tiket: {id_tiket}")
                            for key, value in lihat.items():
                                print(f"{key}: {value}")
                    else:
                        print("Belum ada tiket yang dibeli.")

                elif pilihan == "3":
                    tiket = akuns[username]["tiket"]
                    if tiket:
                        for id_tiket, lihat in tiket.items():
                            print(f"\nID Tiket: {id_tiket}")
                            for key, value in lihat.items():
                                print(f"{key}: {value}")
                    id_tiket = input("Masukkan ID Tiket yang akan diupdate: ")
                    if id_tiket in tiket:
                        nama_penumpang = input("Masukkan Nama Penumpang baru (kosongkan jika tidak ingin mengubah): ")
                        tujuan = input("Masukkan Tujuan baru (kosongkan jika tidak ingin mengubah): ")
                        harga_tiket = input("Masukkan Harga Tiket baru (kosongkan jika tidak ingin mengubah): ")

                        if nama_penumpang:
                            tiket[id_tiket]["Nama Penumpang"] = nama_penumpang
                        if tujuan:
                            tiket[id_tiket]["Tujuan"] = tujuan
                        if harga_tiket:
                            tiket[id_tiket]["Harga Tiket"] = harga_tiket
                        print(f"Tiket dengan ID {id_tiket} berhasil diperbarui.")
                    else:
                        print(f"Tiket dengan ID {id_tiket} tidak ditemukan.")

                elif pilihan == "4":
                    tiket = akuns[username]["tiket"]
                    if tiket:
                        for id_tiket, lihat in tiket.items():
                            print(f"\nID Tiket: {id_tiket}")
                            for key, value in lihat.items():
                                print(f"{key}: {value}")
                    id_tiket = input("Masukkan ID Tiket yang akan dihapus: ")
                    if id_tiket in tiket:
                        del tiket[id_tiket]
                        print(f"Tiket dengan ID {id_tiket} berhasil dihapus.")
                    else:
                        print(f"Tiket dengan ID {id_tiket} tidak ditemukan.")

                elif pilihan == "5":
                    print("Terima kasih telah menggunakan layanan kami!")
                    print()
                    break

                else:
                    print("Pilihan tidak valid, coba lagi.")
        else:
            print("Username atau password salah!")

    elif opsi == "3":
        print("Apakah kamu yakin ingin keluar? ")
        print("1. Iya")
        print("2. Tidak")
        pilih = input("Input pilihan: ")
        print(" ")
        if pilih == "1":
            print("Terima kasih sudah menggunakan layanan pembelian tiket bus, semoga harimu menyenangkan!")
            break
        elif pilih == "2":
            continue
        else:
            print("Input tidak valid, silahkan pilih '1' atau '2'\n")
    else:
        print("Input tidak valid, silahkan pilih 1, 2, atau 3")        

















































































































