akuns = []
pembelian_tiket_bus = {}

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
            if akun[0] == Username:  
                akuna = True
                break
        if akuna:
            print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
        else:
            Password = input("Password: ")
            akuns.append([Username, Password, []])  
            print(f"Akun Anda berhasil terdaftar dengan ID: {Username}")


    elif opsi == "2":
        print("Hi, Silahkan login dulu ya!")
        Username = input("Username: ")
        Password = input("Password: ")
        for akun in akuns:
            if akun[0] == Username and akun[1] == Password:  
                while True:
                    print(f"\nSelamat datang {Username}!")
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
                        pembelian_tiket_bus[id_tiket] = {
                            "Nama Penumpang": nama_penumpang,
                            "Tujuan": tujuan,
                            "Harga Tiket": harga_tiket
                        }
                        print(f"Tiket dengan ID {id_tiket} berhasil ditambahkan.")

                    elif pilihan == "2":
                        if pembelian_tiket_bus:
                            for id_tiket, lihat in pembelian_tiket_bus.items():
                                print(f"\nID Tiket: {id_tiket}")
                                for key, value in lihat.items():
                                    print(f"{key}: {value}")
                        else:
                            print("Belum ada tiket yang dibeli.")

                    elif pilihan == "3":
                        if pembelian_tiket_bus:
                            for id_tiket, lihat in pembelian_tiket_bus.items():
                                print(f"\nID Tiket: {id_tiket}")
                                for key, value in lihat.items():
                                    print(f"{key}: {value}")
                                    print()
                        id_tiket = input("Masukkan ID Tiket yang akan diupdate: ")
                        if id_tiket in pembelian_tiket_bus:
                            nama_penumpang = input("Masukkan Nama Penumpang baru (kosongkan jika tidak ingin mengubah): ")
                            tujuan = input("Masukkan Tujuan baru (kosongkan jika tidak ingin mengubah): ")
                            harga_tiket = input("Masukkan Harga Tiket baru (kosongkan jika tidak ingin mengubah): ")

                            if nama_penumpang:
                                pembelian_tiket_bus[id_tiket]["Nama Penumpang"] = nama_penumpang
                            if tujuan:
                                pembelian_tiket_bus[id_tiket]["Tujuan"] = tujuan
                            if harga_tiket:
                                pembelian_tiket_bus[id_tiket]["Harga Tiket"] = harga_tiket
                            print(f"Tiket dengan ID {id_tiket} berhasil diperbarui.")
                        else:
                            print(f"Tiket dengan ID {id_tiket} tidak ditemukan.")

                    elif pilihan == "4":
                        if pembelian_tiket_bus:
                            for id_tiket, lihat in pembelian_tiket_bus.items():
                                print(f"\nID Tiket: {id_tiket}")
                                for key, value in lihat.items():
                                    print(f"{key}: {value}")
                                    print()
                        id_tiket = input("Masukkan ID Tiket yang akan dihapus: ")
                        if id_tiket in pembelian_tiket_bus:
                            del pembelian_tiket_bus[id_tiket]
                            print(f"Tiket dengan ID {id_tiket} berhasil dihapus.")
                        else:
                            print(f"Tiket dengan ID {id_tiket} tidak ditemukan.")

                    elif pilihan == "5":
                        print("Terima kasih karne sudah mau ngelist")
                        print()
                        break
                    
                    else:
                        print("Pilihan tidak valid, coba lagi.")
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
















































































































