# Class pertama
class Pegawai:

    # Constructor untuk data pegawai
    def __init__(self, id_pegawai, nama, gaji):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.gaji = gaji

    # Method untuk menampilkan data pegawai
    def tampilkan_pegawai(self):
        print("ID Pegawai :", self.id_pegawai)
        print("Nama       :", self.nama)
        print("Gaji       :", self.gaji)


# Class kedua
class PegawaiProyek:

    # Constructor untuk data proyek
    def __init__(self, nama_proyek):
        self.nama_proyek = nama_proyek

    # Method untuk menampilkan data proyek
    def tampilkan_proyek(self):
        print("Nama Proyek :", self.nama_proyek)


# Class ProjectManager mewarisi dua class
class ProjectManager(Pegawai, PegawaiProyek):

    # Constructor ProjectManager
    def __init__(self, id_pegawai, nama, gaji, nama_proyek):
        Pegawai.__init__(self, id_pegawai, nama, gaji)
        PegawaiProyek.__init__(self, nama_proyek)

    # Method untuk menampilkan semua data
    def tampilkan_data(self):
        self.tampilkan_pegawai()
        self.tampilkan_proyek()
        print("-" * 30)


# Membuat object ProjectManager
pm1 = ProjectManager(
    "PM001",
    "Bhisma",
    8000000,
    "Pengembangan Aplikasi Kampus"
)


# Menampilkan data Project Manager
print("DATA PROJECT MANAGER")
pm1.tampilkan_data()
