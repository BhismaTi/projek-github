class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print()


# Membuat minimal tiga object mahasiswa
mahasiswa1 = Mahasiswa("Muhammad Bhisma Kholili", "2595114034")
mahasiswa2 = Mahasiswa("Andi", "2595114035")
mahasiswa3 = Mahasiswa("Budi", "2595114036")

# Memanggil method tampilkan_info() masing-masing object
mahasiswa1.tampilkan_info()
mahasiswa2.tampilkan_info()
mahasiswa3.tampilkan_info()
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def info_buku(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print()


# Membuat dua object
buku1 = Buku("Bulan","tereliye")
buku2 = Buku("Matahari", "tereliye")
buku1.tampilkan_info()
buku2.tampilkan_info()


