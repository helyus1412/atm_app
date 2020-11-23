import random, datetime
from customer import Customer

cust = Customer(id)

# Method Menu
def menu():

    while True:
        print("""
-----------------------------------------
| Selamat Datang di ATM Helmi x Progate |
|                                       |
| 1. Cek Saldo                          |
| 2. Tarik Tunai                        |
| 3. Setor Tunai                        |
| 4. Ubah Pin                           |
| 5. Keluar                             |
-----------------------------------------
""")

        pilih_menu = int(input("\nSilahkan Pilih Menu: "))

        if pilih_menu == 1:
            print("\nsaldo anda: Rp." + str(cust.cek_saldo()))

        elif pilih_menu == 2:
            nominal = float(input("Masukkan nominal: "))
            ver_tarik = input("Apakah anda yakin ingin tarik uang sebanyak: Rp." + str(nominal) + "? (y/n): ")
            if ver_tarik == "y":
                print("\nSaldo awal anda adalah Rp." + str(cust.cek_saldo()))
                if nominal < int(cust.cek_saldo()):
                    cust.tarik_tunai(nominal)
                    print("Penarikan Berhasil, saldo anda saat ini menjadi Rp." + str(cust.cek_saldo()))
                else:
                    print("Maaf saldo anda kurang")
            else:
                break

        elif pilih_menu == 3:
            nominal = float(input("Masukkan nominal: "))
            ver_setor = input("Apakah anda yakin ingin setor uang sebanyak: Rp" + str(nominal) + "? (y/n): ")
            if ver_setor == "y":
                print("\nSaldo awal anda adalah Rp." + str(cust.cek_saldo()))
                cust.setor_tunai(nominal)
                print("Setor tunai berhasil, saldo anda saat ini menjadi Rp." + str(cust.cek_saldo()))
            else:
                break

        elif pilih_menu == 4:

            while True:
                pin_awal = int(input("\nMasukkan Pin Anda: "))
                kesempatan = 1

                while pin_awal != cust.cek_pin() and kesempatan < 3:
                    pin_awal = int(input("Pin yang anda masukkan salah, coba lagi: "))
                    kesempatan += 1
                    if kesempatan == 3:
                        print("\nError. Anda sudah memasukkan pin yang salah sebanyak 3x.")
                        print("Ambil Kartu dan silahkan coba lagi")
                        exit()

                while pin_awal == cust.cek_pin():
                    pin_baru = int(input("\nMasukkan pin baru: "))
                    konfirmasi_pin_baru = int(input("Masukkan lagi pin baru: "))
                    if pin_baru == konfirmasi_pin_baru:
                        cust.update_pin(pin_baru)
                        print("\nPin berhasil di ubah, silahkan masukkan kembali pin anda")
                        verifikasi_pin()
                    else:
                        print("\nPin baru yang anda masukkan tidak sama, silahkan masukkan kembali pin baru anda")

        elif pilih_menu == 5:
            print("\nResi tercetak otomatis saat anda keluar. \nHarap simpan tanda terima ini sebagai bukti transaksi anda.")
            print("\nNo. Rekord: ", random.randint(100000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo akhir: ", cust.cek_saldo())
            print("Terima kasih telah menggunakan ATM Helmi X Progate!")
            exit()

        else:
            print("\nMenu yang anda pilih salah! ")



# Program Utama
def verifikasi_pin():
    while True:
        ver_pin = int(input("\nMasukkan Pin Anda: "))
        kesempatan = 1
        while ver_pin != cust.cek_pin() and kesempatan < 3:
            ver_pin = int(input("Pin yang anda masukkan salah, coba lagi: "))
            kesempatan += 1
            if kesempatan == 3:
                print("\nError. Anda sudah memasukkan pin yang salah sebanyak 3x.")
                print("Ambil Kartu dan silahkan coba lagi")
                exit()
        while True:
            menu()


verifikasi_pin()
