# Class induk
class Kendaraan:

    # Constructor class Kendaraan
    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

    # Method untuk menampilkan data kendaraan
    def tampilkan_kendaraan(self):
        print("Nama       :", self.nama)
        print("Merk       :", self.merk)
        print("Tahun      :", self.tahun)
        print("Kecepatan  :", self.kecepatan, "km/jam")


# Class Mobil mewarisi class Kendaraan
class Mobil(Kendaraan):

    # Constructor class Mobil
    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        super().__init__(nama, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    # Method untuk menampilkan data mobil
    def tampilkan_mobil(self):
        self.tampilkan_kendaraan()
        print("Jumlah Kursi :", self.jumlah_kursi)
        print("-" * 30)


# Class Motor mewarisi class Kendaraan
class Motor(Kendaraan):

    # Constructor class Motor
    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    # Method untuk menampilkan data motor
    def tampilkan_motor(self):
        self.tampilkan_kendaraan()
        print("Tipe Motor   :", self.tipe_motor)
        print("-" * 30)


# Membuat object Mobil
mobil1 = Mobil(
    "Avanza",
    "Toyota",
    2022,
    180,
    7
)

# Membuat object Motor
motor1 = Motor(
    "NMAX",
    "Yamaha",
    2023,
    140,
    "Matic"
)


# Menampilkan data
print("DATA MOBIL")
mobil1.tampilkan_mobil()

print("DATA MOTOR")
motor1.tampilkan_motor()
