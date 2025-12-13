class DataMahasiswa:
    def __init__(self):
        # atribut untuk menyimpan data mahasiswa
        self.data_mahasiswa = {}

    # Method untuk menampilkan data
    def tampilkan(self):
        print("Program Input Nilai")
        print("=" * 65)
        print(f"{('| No').ljust(5)}| {('Nama').ljust(20)}| {('NIM').ljust(10)}| "
              f"{('TUGAS').ljust(6)}| {('UTS').ljust(6)}| {('UAS').ljust(6)}| {('AKHIR').ljust(6)}|")
        print("=" * 65)

        if not self.data_mahasiswa:
            print("|                         TIDAK ADA DATA                        |")
            print("=" * 65)
            return

        no = 1
        for nama, i in self.data_mahasiswa.items():
            print(f"{('| %d' % no).ljust(5)}| {nama.ljust(20)}| {i['nim'].ljust(10)}| "
                  f"{str(i['tugas']).ljust(6)}| {str(i['uts']).ljust(6)}| "
                  f"{str(i['uas']).ljust(6)}| {str(int(i['akhir'])).ljust(6)}|")
            no += 1
        print("=" * 65)

    # Method untuk menambah data
    def tambah(self):
        print("\nTambah Data Mahasiswa")
        nim = input("NIM           : ")
        nama = input("Nama          : ")
        tugas = float(input("Nilai Tugas   : "))
        uts = float(input("Nilai UTS     : "))
        uas = float(input("Nilai UAS     : "))
        akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

        self.data_mahasiswa[nama] = {
            "nim": nim,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": akhir
        }
        print("Data berhasil ditambah!")

    # Method untuk mengubah data
    def ubah(self, nama):
        if nama not in self.data_mahasiswa:
            print("Data tidak ditemukan!")
            return

        print("Data ditemukan. Masukkan data baru:")
        nim = input("Masukkan NIM   : ")
        tugas = float(input("Tugas baru    : "))
        uts = float(input("UTS baru      : "))
        uas = float(input("UAS baru      : "))
        akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

        self.data_mahasiswa[nama] = {
            "nim": nim,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": akhir
        }
        print("Data berhasil diubah!")

    # Method untuk menghapus data
    def hapus(self, nama):
        if nama in self.data_mahasiswa:
            del self.data_mahasiswa[nama]
            print("Data berhasil dihapus!")
        else:
            print("Data tidak ditemukan!")


# ================== PROGRAM UTAMA ==================
data = DataMahasiswa()

while True:
    print("\nProgram Input Nilai")
    print("====================")
    pilihan = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar]: ").lower()

    if pilihan == "l":
        data.tampilkan()
    elif pilihan == "t":
        data.tambah()
    elif pilihan == "u":
        nama = input("\nMasukkan nama yang akan diubah: ")
        data.ubah(nama)
    elif pilihan == "h":
        nama = input("\nMasukkan nama yang akan dihapus: ")
        data.hapus(nama)
    elif pilihan == "k":
        print("Terimakasih sudah menggunakan program ini")
        break
    else:
        print("Pilihan tidak sesuai")
