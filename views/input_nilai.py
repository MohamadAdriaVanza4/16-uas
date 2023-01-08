# Import module daftar nilai dari models
from models import daftar_nilai as daftar

def input_data(no):
    # Input seluruh data
    while True:
        try:
            nim = int(input("Masukan NIM :"))
            if nim == '':
                print("Masukan NIM, tidak boleh kosong")
        except ValueError:
                print("Masukan NIM dengan angka")
        else:
            break

    while True:
        nama = input("Masukan Nama :")
        if nama == '':
            print("Nama tidak boleh kosong")
        else:
            break
    
    while True:
        try:
            tugas = int(input("Masukan Nilai Tugas :"))
            if tugas == '':
                print("Nilai Tugas Tidak Boleh Kosong")
        except ValueError:
            print("Nilai Tugas Berupa Angka")
        else:
            break
    
    while True:
        try:
            uts = int(input("Masukan Nilai UTS :"))
            if uts == '':
                print("Nilai UTS Tidak Boleh Kosong")
        except ValueError:
            print("Nilai UTS Berupa Angka")
        else:
            break
    
    while True:
        try:
            uas = int(input("Masukan Nilai UAS :"))
            if uas == '':
                print("Nilai UAS Tidak Boleh Kosong")
        except ValueError:
            print("Nilai UAS berupa Angka")
        else:
            break
    daftar.tambah_data(no, nim, nama, tugas, uts, uas)