# Membuat class dengan nama Mahasiswa
class Mahasiswa:

    # Constructor untuk mengisi data mahasiswa
    def __init__(self, nama, nim, jurusan, nilai):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.nilai = nilai

    # Method untuk mengecek status kelulusan
    def cek_status(self):
        if self.nilai >= 75:
            return "Lulus"
        else:
            return "Tidak Lulus"

    # Method untuk menampilkan profil mahasiswa
    def tampilkan_profil(self):
        print("Nama     :", self.nama)
        print("NIM      :", self.nim)
        print("Jurusan  :", self.jurusan)
        print("Nilai    :", self.nilai)
        print("Status   :", self.cek_status())
        print("-" * 30)


# Membuat object mahasiswa pertama
mahasiswa1 = Mahasiswa(
    "Bhisma",
    "2595114034",
    "Teknik Informatika",
    85
)

# Membuat object mahasiswa kedua
mahasiswa2 = Mahasiswa(
    "Andi",
    "2595114035",
    "Teknik Informatika",
    70
)

# Membuat object mahasiswa ketiga
mahasiswa3 = Mahasiswa(
    "Budi",
    "2595114036",
    "Sistem Informasi",
    78
)


# Menampilkan semua profil mahasiswa
mahasiswa1.tampilkan_profil()
mahasiswa2.tampilkan_profil()
mahasiswa3.tampilkan_profil()
