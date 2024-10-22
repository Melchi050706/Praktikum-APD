import os
akuns = {}
user_logged_in = None

def clear_screen():
    os.system('cls || clear')

def main_menu():
    while True:
        clear_screen()
        print("Halo! Selamat datang di list pembelian tiket bus")
        print("Silakan pilih 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
        print("1. Daftar akun")
        print("2. Login")
        print("3. Exit")
        print("――――――――――――――――――――――――")
        opsi = input("Pilih opsi: ")
        print(" ")
        
        if opsi == "1":
            Daftar_akun()
        elif opsi == "2":
            Login_akun()
        elif opsi == "3":
            Exit()
        else:
            print("Input tidak valid, silahkan pilih 1, 2, atau 3")

def Daftar_akun():
    clear_screen()
    print("Halo Pengguna baru! Ayo buat akun dulu")
    username = input("Username: ")
    if username in akuns:
        print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
        input("untuk melanjutkan klik Enter.....")
    else:
        password = input("Password: ")
        akuns[username] = {"password": password, "tiket": {}}
        print(f"Akun Anda berhasil terdaftar dengan ID: {username}")
        input("untuk melanjutkan klik Enter.....")

def Login_akun():
    global user_logged_in
    clear_screen()
    print("Hi, Silahkan login dulu ya!")
    username = input("Username: ")
    password = input("Password: ")
    
    if username in akuns and akuns[username]["password"] == password:
        user_logged_in = username
        ticket_menu()
    else:
        print("Username atau password salah!")

def ticket_menu():
    while True:
        clear_screen()
        print(f"\nSelamat datang {user_logged_in}!")
        print("\n=== Menu Pembelian Tiket Bus ===")
        print("1. Tambah Tiket")
        print("2. Lihat Tiket")
        print("3. Ubah Tiket")
        print("4. Hapus Tiket")
        print("5. Keluar")
        print("_____________________")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            Tambah_tiket()
        elif pilihan == "2":
            Lihat_tiket()
        elif pilihan == "3":
            Ubah_tiket()
        elif pilihan == "4":
            Hapus_tiket()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan layanan kami!")
            input("untuk melanjutkan klik Enter.....")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

def Tambah_tiket():
    clear_screen()
    id_tiket = input("Masukkan ID Tiket: ")
    nama_penumpang = input("Masukkan Nama Penumpang: ")
    tujuan = input("Masukkan Tujuan: ")
    harga_tiket = input("Masukkan Harga Tiket: ")
    
    akuns[user_logged_in]["tiket"][id_tiket] = {
        "Nama Penumpang": nama_penumpang,
        "Tujuan": tujuan,
        "Harga Tiket": harga_tiket
    }
    print(f"Tiket dengan ID {id_tiket} berhasil ditambahkan.")

def Lihat_tiket():
    clear_screen()
    tiket = akuns[user_logged_in]["tiket"]
    if tiket:
        for id_tiket, detail in tiket.items():
            print(f"\nID Tiket: {id_tiket}")
            for key, value in detail.items():
                print(f"{key}: {value}")
    else:
        print("Belum ada tiket yang dibeli.")

    input("untuk melanjutkan klik Enter.....")

def Ubah_tiket():
    clear_screen()
    tiket = akuns[user_logged_in]["tiket"]
    if tiket:
        for id_tiket in tiket.keys():
            print(f"\nID Tiket: {id_tiket}")

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
    else:
        print("Belum ada tiket yang dibeli.")

    input("untuk melanjutkan klik Enter.....")

def Hapus_tiket():
    clear_screen()
    tiket = akuns[user_logged_in]["tiket"]
    if tiket:
        for id_tiket in tiket.keys():
            print(f"\nID Tiket: {id_tiket}")

        id_tiket = input("Masukkan ID Tiket yang akan dihapus: ")
        if id_tiket in tiket:
            del tiket[id_tiket]
            print(f"Tiket dengan ID {id_tiket} berhasil dihapus.")
        else:
            print(f"Tiket dengan ID {id_tiket} tidak ditemukan.")
    else:
        print("Belum ada tiket yang dibeli.")

    input("untuk melanjutkan klik Enter.....")

def Exit():
    clear_screen()
    print("Apakah kamu yakin ingin keluar? ")
    print("1. Iya")
    print("2. Tidak")
    pilih = input("Input pilihan: ")
    print(" ")
    
    if pilih == "1":
        print("Terima kasih sudah menggunakan layanan pembelian tiket bus, semoga harimu menyenangkan!")
        exit()
    elif pilih == "2":
        return
    else:
        print("Input tidak valid, silahkan pilih '1' atau '2'\n")
        Exit()  

if __name__ == "__main__":
    main_menu()

