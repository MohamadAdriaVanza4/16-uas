from views import view_nilai
from tabulate import tabulate

dataMahasiswa = {
    'No': [],
    'Nim': [],
    'Nama': [],
    'Tugas': [],
    'Uts': [],
    'Uas': [],
    'Nilai Akhir': []
}

# Fungsi mengembalikan dataMahasiswa

def Index():
    return dataMahasiswa


# Fungsi tambah data

def tambah_data(no, nim, nama, tugas, uts, uas):
    nilai_akhir = tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100
    # menambahkan data
    dataMahasiswa['No'].append(no)
    dataMahasiswa['Nim'].append(nim)
    dataMahasiswa['Nama'].append(nama)
    dataMahasiswa['Tugas'].append(tugas)
    dataMahasiswa['Uts'].append(uts)
    dataMahasiswa['Uas'].append(uas)
    dataMahasiswa['Nilai Akhir'].append(nilai_akhir)
    print('Data berhasil ditambahkan.')

    # Fungsi untuk ubah data

def ubah_data():
    # Print data untuk referensi nim pada data yang ingin dihapus
    print(tabulate(dataMahasiswa, headers=[
        'No', 'Nim', 'Nama', 'Tugas', 'UTS', 'UAS', 'Nilai Akhir'], tablefmt="fancy_grid"))

    # Cek jika nama tersebut di dataMahasiswa
    nim = int(input('Masukan Nim yang mau diedit :'))

    if nim in dataMahasiswa['Nim']:
        # Cari posisi indexnya lalu disimpan di nimIndex
        nimIndex = dataMahasiswa['Nim'].index(nim)
        print("Pilih data yang mau di edit")
        # Perulangan mengedit data dalam bentuk pilihan
        while True:
            editApa = int(input(
                "(1) NIM , | (2) Nama, | (3) Nilai Tugas, | (4) Nilai UTS, | (5) Nilai UAS, | (0) Simpan Perubahan & Keluar : \n"))
            print("")
            
            if editApa == 1:
                # jika memilih opsi 1 merubah nim
                newNim = int(input("Masukan Nim :"))
                dataMahasiswa['Nim'][nimIndex] = newNim
            elif editApa == 2:
                # jika memilih opsi 2 merubah nama
                newNama = input("Masukan Nama :")
                dataMahasiswa['Nama'][nimIndex] = newNama
            elif editApa == 3:
                # jika memilih opsi 3 merubah nilai tugas & nilai akhir
                newTugas = int(input("Masukan Nilai Tugas :"))
                # memperbarui nilai akhir
                nilai_akhir = (newTugas * 30 / 100) + (dataMahasiswa['Uts'][nimIndex] * 35 / 100) + (
                    dataMahasiswa['Uas'][nimIndex] * 35 / 100)
                dataMahasiswa['Tugas'][nimIndex] = newTugas
                dataMahasiswa['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa == 4:
                # jika memilih opsi 4 merubah nilai uts & nilai akhir
                newUts = int(input("Masukan Nilai Uts :"))
                # memperbarui nilai akhir
                nilai_akhir = (dataMahasiswa['Tugas'][nimIndex] * 30 / 100) + (newUts * 35 / 100) + (
                    dataMahasiswa['Uas'][nimIndex] * 35 / 100)
                dataMahasiswa['Uts'][nimIndex] = newUts
                dataMahasiswa['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa == 5:
                # jika memilih opsi 5 merubah nilai uas & nilai akhir
                newUas = int(input("Masukan Nilai Uas :"))
                # memperbarui nilai akhir
                nilai_akhir = (dataMahasiswa['Tugas'][nimIndex] * 30 / 100) + (dataMahasiswa['Uts'][nimIndex] * 35 / 100) + (
                    newUas * 35 / 100)
                dataMahasiswa['Uas'][nimIndex] = newUas
                dataMahasiswa['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa == 0:
                # jika memilih opsi 0 menyimpan perubahan dan keluar dari edit data
                print('Perubahan Data berhasil disimpan,')
                break

            else:
                print("Data tidak ditemukan")

# Fungsi untuk mencari data

def cari_data():

    nama = input('Masukan nama yang ingin dicari :')
    # Cek jika nama ada di dataMahasiswa cari lokasi indexnya
    if nama in dataMahasiswa['Nama']:
        namaIndex = dataMahasiswa['Nama'].index(nama)
        # simpan data di variabel hasilPencarian pada posisi index yang telah di tentukan
        hasilPencarian ={
            'No': [dataMahasiswa['No'][namaIndex]],
            'Nim': [dataMahasiswa['Nim'][namaIndex]],
            'Nama': [dataMahasiswa['Nama'][namaIndex]],
            'Tugas': [dataMahasiswa['Tugas'][namaIndex]],
            'UTS': [dataMahasiswa['Uts'][namaIndex]],
            'UAS': [dataMahasiswa['Uas'][namaIndex]],
            'Nilai Akhir': [dataMahasiswa['Nilai Akhir'][namaIndex]]
        }
        # Memparsing parameter hasil dari pencarian ke modul cek hasil pencarian
        view_nilai.cetak_hasil_pencarian(hasilPencarian)
    else:
        print("Data tidak ditemukan")

# Fungsi untuk menghapus data

def hapus_data():
    # Print data untuk referensi nim pada data yang ingin di hapus
    print(tabulate(dataMahasiswa, headers=[
        'No', 'Nim', 'Nama', 'Tugas', 'UTS', 'UAS', 'Nilai Akhir'],tablefmt="fancy_grid"))
    nim = int(input('Masukan NIM yang ingin dihapus :'))
    # cek jika nim yang ingin dihapus pada dataMahasiswa
    if nim in dataMahasiswa['Nim']:
        nimIndex = dataMahasiswa['Nim'].index(nim)
        # menghapus data mahasiswa berdasarkan posisi index yang telah ditemukan
        del dataMahasiswa['No'][nimIndex]
        del dataMahasiswa['Nim'][nimIndex]
        del dataMahasiswa['Nama'][nimIndex]
        del dataMahasiswa['Tugas'][nimIndex]
        del dataMahasiswa['Uts'][nimIndex]
        del dataMahasiswa['Uas'][nimIndex]
        del dataMahasiswa['Nilai Akhir'][nimIndex]
        print("Data Berhasil Dihapus")
    else:
        print("Data tidak di temukan")