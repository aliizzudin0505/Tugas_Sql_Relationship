import csv
import random
import string
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_dummy_data(num_records):
    id_counter = { # Inisialisasi penghitung ID
        'merek': 1,
        'jenis_body': 1,
        'model': 1,
        'pengguna': 1,
        'domisili': 1,
        'produk': 1
    }

    data = {
        'pengguna': [],
        'merek': [],
        'model': [],
        'jenis_body': [],
        'domisili': [], 
        'produk': [],
    }

    # Generate data for 'pengguna' table
    roles = ['Penjual', 'Pembeli']
    status_akun = ['Aktif', 'Tidak Aktif']
    for _ in range(num_records):
        data['pengguna'].append({
            'ID': id_counter['pengguna'],
            'Nama': fake.name(),
            'Kontak': fake.phone_number(),
            'Role': random.choice(roles),
            'Username': fake.user_name(),
            'Password': fake.password(),
            'Email': fake.email(),
            'Foto_Profil': None,
            'Tanggal_Registrasi': fake.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%d %H:%M:%S'),
            'Status_Akun': random.choice(status_akun),
            'Domisili_ID': random.randint(1, 50), 
        })
        id_counter['pengguna'] += 1  # Increment ID


    # Generate data for 'merek' table
    car_brands = ['Toyota', 'Honda', 'Suzuki', 'Daihatsu', 'Mitsubishi', 'Nissan', 'Mazda', 'BMW', 'Mercedes-Benz', 'Audi']
    for brand in car_brands:
        data['merek'].append({'ID': id_counter['merek'],'Nama': brand})
        id_counter['merek'] += 1  # Increment ID

    # Generate data for 'model' table
    car_models = {
        'Toyota': ['Avanza', 'Innova', 'Fortuner', 'Yaris', 'Rush', 'Calya', 'Agya', 'Vios', 'Camry', 'Corolla Altis'],
        'Honda': ['Brio', 'Mobilio', 'BR-V', 'HR-V', 'CR-V', 'Civic', 'Accord', 'City', 'Jazz', 'Odyssey'],
        'Suzuki': ['Ertiga', 'XL7', 'Ignis', 'Baleno', 'Swift', 'Karimun Wagon R', 'APV', 'Grand Vitara', 'Jimny', 'SX4'],
        'Daihatsu': ['Xenia', 'Terios', 'Ayla', 'Sigra', 'Sirion', 'Gran Max', 'Luxio', 'Rocky', 'Mira', 'Copen'],
        'Mitsubishi': ['Xpander', 'Pajero Sport', 'Triton', 'Outlander', 'Mirage', 'Eclipse Cross', 'L300', 'Colt', 'Fuso', 'Delica'],
        'Nissan': ['Livina', 'X-Trail', 'Terra', 'Navara', 'Serena', 'Juke', 'Almera', 'March', 'GT-R', '370Z'],
        'Mazda': ['CX-5', 'Mazda2', 'Mazda3', 'CX-3', 'CX-8', 'CX-9', 'MX-5', 'BT-50', '6', 'RX-8'],
        'BMW': ['3 Series', '5 Series', 'X1', 'X3', 'X5', '7 Series', 'Z4', 'M3', 'M5', 'i8'],
        'Mercedes-Benz': ['C-Class', 'E-Class', 'GLC', 'GLE', 'S-Class', 'A-Class', 'CLA', 'GLA', 'G-Class', 'AMG GT'],
        'Audi': ['A3', 'A4', 'Q3', 'Q5', 'Q7', 'A6', 'A8', 'TT', 'R8', 'e-tron']
    }

    for brand in car_brands:
        for model in car_models.get(brand, []):
            data['model'].append({
                'ID': id_counter['model'],
                'Merek_ID': car_brands.index(brand) + 1,
                'Nama': model
            })
            id_counter['model'] += 1  # Increment ID

    # Generate data for 'jenis_body' table
    car_body_types = ['Sedan', 'Hatchback', 'SUV', 'MPV', 'Pickup', 'Coupe', 'Convertible', 'Wagon', 'Van', 'Minibus']
    for body_type in car_body_types:
        data['jenis_body'].append({
            'ID': id_counter['jenis_body'],
            'Nama': body_type
            })
        id_counter['jenis_body'] += 1

    # Generate data for 'domisili' table
    provinces = ["Aceh", "Sumatra Utara", "Sumatra Barat", "Riau", "Kepulauan Riau", 
                "Jambi", "Sumatra Selatan", "Bangka Belitung", "Bengkulu", "Lampung", 
                "DKI Jakarta", "Jawa Barat", "Banten", "Jawa Tengah", "DI Yogyakarta", 
                "Jawa Timur", "Bali", "Nusa Tenggara Barat", "Nusa Tenggara Timur", 
                "Kalimantan Barat", "Kalimantan Tengah", "Kalimantan Selatan", 
                "Kalimantan Timur", "Kalimantan Utara", "Sulawesi Utara", 
                "Sulawesi Tengah", "Sulawesi Selatan", "Sulawesi Tenggara", "Gorontalo", 
                "Sulawesi Barat", "Maluku", "Maluku Utara", "Papua Barat", "Papua"]

    for _ in range(50): 
        province = random.choice(provinces)
        city = fake.city()
        latitude = round(random.uniform(-10, 10), 8) 
        longitude = round(random.uniform(95, 141), 8) 

        data['domisili'].append({
            'ID': id_counter['domisili'], 
            'Provinsi': province,
            'Kota': city,
            'Latitude': latitude,
            'Longitude': longitude
        })
        id_counter['domisili'] += 1

    # Generate data for 'produk' table
    transmissions = ['Manual', 'Automatic']
    status_produk = ['Tersedia', 'Terjual', 'Dalam Negosiasi']
    colors = ['Hitam', 'Putih', 'Silver', 'Abu-abu', 'Merah', 'Biru', 'Hijau', 'Kuning', 'Oranye', 'Coklat']
    conditions = ['Bekas', 'Seperti Baru', 'Bagus', 'Lumayan', 'Perlu Perbaikan']
    for _ in range(num_records):
        merek_id = random.randint(1, len(car_brands))

        available_models = car_models.get(car_brands[merek_id - 1], [])
        if not available_models: 
            merek_id = random.randint(1, len(car_brands))
            available_models = car_models.get(car_brands[merek_id - 1], [])

        model_id = random.randint(1, len(available_models))
        jenis_body_id = random.randint(1, len(car_body_types))
        tahun_pembuatan = random.randint(1990, datetime.now().year)
        harga = round(random.uniform(100000000, 1000000000), 2) 

        data['produk'].append({
            'ID': id_counter['produk'],
            'Merek_ID': merek_id,
            'Model_ID': model_id,
            'JenisBody_ID': jenis_body_id,
            'Tipe_Transmisi': random.choice(transmissions),
            'TahunPembuatan': tahun_pembuatan,
            'Warna': random.choice(colors),
            'JarakTempuh': random.randint(10000, 200000),
            'Plat_Nomer': fake.license_plate(),
            'Kondisi': random.choice(conditions),
            'Harga': harga,
            'Foto': 'path/to/default_image.jpg', 
            'Status': random.choice(status_produk),
            'Tanggal_Posting': fake.date_this_year().strftime('%Y-%m-%d'),
            'Kapasitas_Mesin': random.randint(1000, 3000),
            'Fitur_Khusus': fake.sentence(),
            'Penjual_ID': random.randint(1, num_records), 
        })
        id_counter['produk'] += 1

    return data

def save_to_csv(data, filename):
    for table_name, table_data in data.items():
        with open(f'{filename}_{table_name}.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = table_data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
            writer.writeheader()
            writer.writerows(table_data)
# Fungsi untuk membuat data dummy realistis untuk tabel Iklan
def generate_iklan_data(i):
    with open('penjualan_mobil_bekas_produk.csv', 'r') as f:
        produk_reader = csv.DictReader(f)
        produk_data = list(produk_reader)
    with open('penjualan_mobil_bekas_pengguna.csv', 'r') as f:
        pengguna_reader = csv.DictReader(f)
        pengguna_data = list(pengguna_reader)

    return {
        'ID': i + 1,
        'Pengguna_ID': random.choice(pengguna_data)['ID'],
        'Produk_ID': random.choice(produk_data)['ID'],
        'Judul': f"{random.choice(produk_data)['Merek_ID']} {random.choice(produk_data)['Model_ID']} Bekas Kondisi Prima",
        'Deskripsi': fake.paragraph(nb_sentences=3),
        'KontakPenjual': fake.phone_number(),
        'IzinkanBid': random.choice([True, False]),
        'Catatan': fake.sentence() if random.random() < 0.5 else ""
    }

# Fungsi untuk membuat data dummy realistis untuk tabel Bid
def generate_bid_data(i):
    with open('penjualan_mobil_bekas_iklan.csv', 'r') as f:
        iklan_reader = csv.DictReader(f)
        iklan_data = list(iklan_reader)
    with open('penjualan_mobil_bekas_pengguna.csv', 'r') as f:
        pengguna_reader = csv.DictReader(f)
        pengguna_data = list(pengguna_reader)

    return {
        'ID': i + 1,
        'Iklan_ID': random.choice(iklan_data)['ID'],
        'Pengguna_ID': random.choice(pengguna_data)['ID'],
        'Harga': round(random.uniform(100000000, 1000000000), 2),
        'Tanggal': fake.date_time_between(start_date='-30d', end_date='now').strftime('%Y-%m-%d %H:%M:%S'),
        'Status': random.choice(['Pending', 'Diterima', 'Ditolak'])
    }

# Fungsi untuk membuat data dummy realistis untuk tabel RiwayatBid
def generate_riwayat_bid_data(i):
    with open('penjualan_mobil_bekas_bid.csv', 'r') as f:
        bid_reader = csv.DictReader(f)
        bid_data = list(bid_reader)

    return {
        'ID': i + 1,
        'Bid_ID': random.choice(bid_data)['ID'],
        'UrutanBid': random.randint(1, 5),
        'HargaBid': round(random.uniform(100000000, 1000000000), 2),
        'TanggalBid': fake.date_time_between(start_date='-30d', end_date='now').strftime('%Y-%m-%d %H:%M:%S')
    }

# Fungsi untuk membuat data dummy realistis untuk tabel Review
def generate_review_data(i):
    with open('penjualan_mobil_bekas_pengguna.csv', 'r') as f:
        pengguna_reader = csv.DictReader(f)
        pengguna_data = list(pengguna_reader)

    return {
        'ID': i + 1,
        'Pengguna_ID': random.choice(pengguna_data)['ID'],
        'Penjual_ID': random.choice(pengguna_data)['ID'],
        'Rating': random.randint(1, 5),
        'Komentar': fake.sentence() if random.random() < 0.8 else "",
        'Tanggal': fake.date_time_between(start_date='-30d', end_date='now').strftime('%Y-%m-%d %H:%M:%S')
    }

# Fungsi untuk membuat data dummy realistis untuk tabel Wishlist
def generate_wishlist_data(i):
    with open('penjualan_mobil_bekas_pengguna.csv', 'r') as f:
        pengguna_reader = csv.DictReader(f)
        pengguna_data = list(pengguna_reader)
    with open('penjualan_mobil_bekas_produk.csv', 'r') as f:
        produk_reader = csv.DictReader(f)
        produk_data = list(produk_reader)

    return {
        'ID': i + 1,
        'Pengguna_ID': random.choice(pengguna_data)['ID'],
        'Produk_ID': random.choice(produk_data)['ID']
    }

if __name__ == '__main__':
    num_records = 50
    dummy_data = generate_dummy_data(num_records)
    save_to_csv(dummy_data, 'penjualan_mobil_bekas')
    
    
    tables = {
        'Iklan': generate_iklan_data,
        'Bid': generate_bid_data,
        'RiwayatBid': generate_riwayat_bid_data,
        'Review': generate_review_data,
        'Wishlist': generate_wishlist_data
    }

    for table_name, generate_func in tables.items():
        with open(f'penjualan_mobil_bekas_{table_name.lower()}.csv', 'w', newline='') as f:
            fieldnames = list(generate_func(0).keys()) 
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(num_records):
                writer.writerow(generate_func(i))