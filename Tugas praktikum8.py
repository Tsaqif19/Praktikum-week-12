data_mahasiswa = {}

def data():
    nim = input("NIM           : ")
    nama = input("Nama          : ") 
    tugas = float(input("Nilai Tugas   : "))
    uts = float(input("Nilai UTS     : "))
    uas = float(input("Nilai UAS     : "))
    akhir = (tugas*0.3) + (uts*0.35) + (uas*0.35)

    data_mahasiswa[nama] = {
        "nim": nim,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": akhir
    }

class tampilkan_data_mahasiswa:
    def tampilkan():
        print("Program Input Nilai")
        print("=" * 65)
        print(f"{('| No').ljust(5)}| {('Nama').ljust(20)}| {('NIM').ljust(10)}| {('TUGAS').ljust(6)}| {('UTS').ljust(6)}| {('UAS').ljust(6)}| {('AKHIR').ljust(6)}|")
        print("=" * 65)

        if not data_mahasiswa:
            print("|                         TIDAK ADA DATA                        |")
            print("="*65)
            return
    
        no = 1
        for nama, i in data_mahasiswa.items():
            print(f"{('| %d'%no).ljust(5)}| {str(nama).ljust(20)}| {(i['nim']).ljust(10)}| {str(i['tugas']).ljust(6)}| {str(i['uts']).ljust(6)}| {str(i['uas']).ljust(6)}| {str('%d'%i['akhir']).ljust(6)}|",end="\n")
            no += 1
        print("="*65)


    def tambah():
        data()
        print ("Data berhasil ditambah!")

def ubah(nama):
    if nama not in data_mahasiswa:
        print ("Data tidak ditemukan!")
        return
    
    print ("Data ditemukan, Silahkan masukkan data baru")


    



while True:
    print("\nProgram Input Nilai")
    print("====================")
    pilihan = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar]: ").lower()

    if pilihan == "l":
        tampilkan()
    elif pilihan == "t":
        tambah()


    

