# Program CRUD Makanan dan Minuman dengan Login dan Pendaftaran

# Daftar untuk menyimpan makanan dan minuman
menu = []

# Daftar untuk menyimpan pembelian
pembelian = []

# Daftar untuk menyimpan akun pembeli
akun_pembeli = {}

# Akun penjual tetap
akun_penjual = {'username': 'kelompok 3', 'password': 'samarinda2024'}

# Fungsi untuk menambahkan makanan dan minuman awal
def tambahkan_makanan_dan_minuman_awal():
    items = [
        {'nama': 'Nasi Goreng', 'harga': 25000},
        {'nama': 'Mie Goreng', 'harga': 20000},
        {'nama': 'Sate Ayam', 'harga': 30000},
        {'nama': 'Es Teh Manis', 'harga': 5000},
        {'nama': 'Kopi', 'harga': 10000},
        {'nama': 'Ayam Penyet', 'harga': 35000},
    ]
    menu.extend(items)
    print("Makanan dan minuman awal berhasil ditambahkan ke menu.")

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\nMenu Makanan dan Minuman:")
    if not menu:
        print("Menu kosong.")
    else:
        for i, item in enumerate(menu):
            # Menambahkan format Rupiah dengan koma
            harga_format = f"Rp.{item['harga']:,.0f}"
            print(f"{i + 1}. {item['nama']} - Harga: {harga_format}")

# Fungsi untuk menambah makanan dan minuman
def tambah_menu():
    while True:
        try:
            nama = input("Masukkan nama makanan/minuman (ketik 'selesai' untuk keluar): ")
            if nama.lower() == 'selesai':
                break
            harga = float(input("Masukkan harga makanan/minuman: "))
            menu.append({'nama': nama, 'harga': harga})
            print("Makanan/minuman berhasil ditambahkan.")
        except ValueError:
            print("Harap masukkan nilai harga yang valid.")

# Fungsi untuk mengubah makanan dan minuman
def ubah_menu():
    tampilkan_menu()
    try:
        index = int(input("Masukkan nomor item yang ingin diubah: ")) - 1
        if 0 <= index < len(menu):
            nama = input("Masukkan nama baru: ")
            harga = float(input("Masukkan harga baru: "))
            menu[index] = {'nama': nama, 'harga': harga}
            print("Makanan/minuman berhasil diubah.")
        else:
            print("Nomor item tidak valid.")
    except ValueError:
        print("Harap masukkan nilai yang valid.")

# Fungsi untuk menghapus makanan dan minuman
def hapus_menu():
    tampilkan_menu()
    try:
        index = int(input("Masukkan nomor item yang ingin dihapus: ")) - 1
        if 0 <= index < len(menu):
            menu.pop(index)
            print("Makanan/minuman berhasil dihapus.")
        else:
            print("Nomor item tidak valid.")
    except ValueError:
        print("Harap masukkan nilai yang valid.")

# Fungsi untuk membeli makanan dan minuman
def beli_menu(saldo):
    tampilkan_menu()
    try:
        index = int(input("Masukkan nomor item yang ingin dibeli: ")) - 1
        if 0 <= index < len(menu):
            total_harga = menu[index]['harga']
            if saldo >= total_harga:
                pembelian.append(menu[index])
                saldo -= total_harga
                # Menambahkan format Rupiah dengan koma
                print(f"Anda telah membeli: {menu[index]['nama']}.")
                print(f"Sisa saldo Anda: Rp.{saldo:,.0f}")
            else:
                print("Saldo Anda tidak cukup.")
        else:
            print("Nomor item tidak valid.")
    except ValueError:
        print("Harap masukkan nilai yang valid.")
    
    return saldo

# Fungsi untuk menampilkan pembelian
def tampilkan_pembelian():
    print("\nDaftar Pembelian:")
    if not pembelian:
        print("Belum ada pembelian.")
    else:
        total = 0
        for item in pembelian:
            # Menambahkan format Rupiah dengan koma
            harga_format = f"Rp.{item['harga']:,.0f}"
            print(f"- {item['nama']} - Harga: {harga_format}")
            total += item['harga']
        # Menambahkan format Rupiah dengan koma pada total
        print(f"Total Pembelian: Rp.{total:,.0f}")

# Fungsi untuk mendaftar akun pembeli
def daftar_akun_pembeli():
    while True:
        username = input("Masukkan username: ").strip()
        if not username:
            print("Error: Username tidak boleh kosong.")
            continue

        if username in akun_pembeli:
            print("Error: Username sudah terdaftar.")
            continue

        password = input("Masukkan password: ").strip()
        if not password:
            print("Error: Password tidak boleh kosong.")
            continue
        
        akun_pembeli[username] = password
        print(f"Akun pembeli berhasil dibuat dengan ID: {username}")
        break

# Fungsi untuk login
def login():
    username = input("Masukkan username: ").strip()
    if not username:
        print("Error: Username tidak boleh kosong.")
        return None

    password = input("Masukkan password: ").strip()
    if not password:
        print("Error: Password tidak boleh kosong.")
        return None

    if username == akun_penjual['username'] and password == akun_penjual['password']:
        print("Login berhasil sebagai penjual!")
        return 'penjual'
    elif akun_pembeli.get(username) == password:
        print("Login berhasil sebagai pembeli!")
        return 'pembeli'
    else:
        print("Error: Username atau password salah.")
        return None

# Fungsi utama
def main():
    # Tambahkan makanan dan minuman awal
    tambahkan_makanan_dan_minuman_awal()

    while True:
        print("\n=== Sistem Makanan dan Minuman ===")
        print("1. Daftar Akun Pembeli")
        print("2. Login")
        print("3. Keluar")
        print("________________________________________")

        pilihan = input("Pilih aksi (1-3): ")

        if pilihan == '1':
            daftar_akun_pembeli()
        elif pilihan == '2':
            role = login()
            if role == 'penjual':
                while True:
                    print("\nMenu Penjual:")
                    print("1. Tambah Makanan/Minuman")
                    print("2. Ubah Makanan/Minuman")
                    print("3. Hapus Makanan/Minuman")
                    print("4. Lihat Menu")
                    print("5. Keluar")
                    print("______________________________")
                    
                    try:
                        pilihan = int(input("Pilih aksi (1-5): "))
                        if pilihan == 1:
                            tambah_menu()
                        elif pilihan == 2:
                            ubah_menu()
                        elif pilihan == 3:
                            hapus_menu()
                        elif pilihan == 4:
                            tampilkan_menu()
                        elif pilihan == 5:
                            break
                        else:
                            print("Pilihan tidak valid.")
                    except ValueError:
                        print("Harap masukkan pilihan yang valid.")

            elif role == 'pembeli':
                while True:
                    try:
                        saldo = float(input("Masukkan jumlah saldo Anda: Rp."))
                        if saldo < 0:
                            print("Error: Saldo tidak boleh bernilai negatif. Silakan masukkan saldo yang valid.")
                            continue
                        break
                    except ValueError:
                        print("Error: Harap masukkan nilai saldo yang valid.")

                while True:
                    print("\nMenu Pembeli:")
                    print("1. Beli Makanan/Minuman")
                    print("2. Lihat Pembelian")
                    print("3. Keluar")
                    print("______________________________")

                    try:
                        pilihan = int(input("Pilih aksi (1-3): "))
                        if pilihan == 1:
                            saldo = beli_menu(saldo)
                        elif pilihan == 2:
                            tampilkan_pembelian()
                        elif pilihan == 3:
                            break
                        else:
                            print("Pilihan tidak valid.")
                    except ValueError:
                        print("Harap masukkan pilihan yang valid.")

        elif pilihan == '3':
            print("Terima kasih sudah menggunakan sistem ini. Semoga hari Anda menyenangkan!")
            break
        else:
            print("Pilihan tidak valid.")

main()
