-- Tabel Domisili
CREATE TABLE "Domisili" (
    "ID" SERIAL PRIMARY KEY,
    "Provinsi" VARCHAR(255) NOT NULL,
    "Kota" VARCHAR(255) NOT NULL,
    "Latitude" DECIMAL(10, 8) NOT NULL,
    "Longitude" DECIMAL(11, 8) NOT NULL
);


-- Tabel Pengguna
CREATE TABLE "Pengguna" (
    "ID" SERIAL PRIMARY KEY,
    "Nama" VARCHAR(255) NOT NULL,
    "Kontak" VARCHAR(255) NOT NULL,
    "Role" VARCHAR(255) CHECK ("Role" IN ('Penjual', 'Pembeli')) NOT NULL, 
    "Username" VARCHAR(255) UNIQUE,
    "Password" CHAR(60) NOT NULL,
    "Email" VARCHAR(255) UNIQUE,
    "Foto_Profil" TEXT,
    "Tanggal_Registrasi" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "Status_Akun" VARCHAR(255) CHECK ("Status_Akun" IN ('Aktif', 'Tidak Aktif')) NOT NULL DEFAULT 'Aktif', 
    "Domisili_ID" INT NOT NULL,
    FOREIGN KEY ("Domisili_ID") REFERENCES "Domisili"("ID")
);

-- Tabel Merek
CREATE TABLE "Merek" (
    "ID" SERIAL PRIMARY KEY,
    "Nama" VARCHAR(255) NOT NULL
);

-- Tabel Model
CREATE TABLE "Model" (
    "ID" SERIAL PRIMARY KEY,
    "Merek_ID" INT NOT NULL,
    "Nama" VARCHAR(255) NOT NULL,
    FOREIGN KEY ("Merek_ID") REFERENCES "Merek"("ID")
);

-- Tabel JenisBody
CREATE TABLE "JenisBody" (
    "ID" SERIAL PRIMARY KEY,
    "Nama" VARCHAR(255) NOT NULL
);


-- Tabel Produk
CREATE TABLE "Produk" (
    "ID" SERIAL PRIMARY KEY,
    "Merek_ID" INT NOT NULL,
    "Model_ID" INT NOT NULL,
    "JenisBody_ID" INT NOT NULL,
    "Tipe_Transmisi" VARCHAR(255) CHECK ("Tipe_Transmisi" IN ('Manual', 'Automatic')) NOT NULL,
    "TahunPembuatan" SMALLINT NOT NULL CHECK ("TahunPembuatan" <= EXTRACT(YEAR FROM CURRENT_DATE)), 
    "Warna" VARCHAR(255) NOT NULL,
    "JarakTempuh" INT NOT NULL CHECK ("JarakTempuh" >= 0),
    "Plat_Nomer" VARCHAR(20) UNIQUE NOT NULL,
    "Kondisi" VARCHAR(255) NOT NULL,
    "Harga" DECIMAL(15,2) NOT NULL CHECK ("Harga" > 0),
    "Foto" VARCHAR(512) NOT NULL,
    "Status" VARCHAR(255) CHECK ("Status" IN ('Tersedia', 'Terjual', 'Dalam Negosiasi')) NOT NULL DEFAULT 'Tersedia', 
    "Tanggal_Posting" DATE DEFAULT CURRENT_DATE,
    "Kapasitas_Mesin" INT NOT NULL CHECK ("Kapasitas_Mesin" > 0),
    "Fitur_Khusus" TEXT,
    "Penjual_ID" INT NOT NULL,
    FOREIGN KEY ("Merek_ID") REFERENCES "Merek"("ID"),
    FOREIGN KEY ("Model_ID") REFERENCES "Model"("ID"),
    FOREIGN KEY ("JenisBody_ID") REFERENCES "JenisBody"("ID"),
    FOREIGN KEY ("Penjual_ID") REFERENCES "Pengguna"("ID")
);

-- Menambahkan indeks pada kolom-kolom yang sering digunakan dalam pencarian
CREATE INDEX "idx_produk_merek" ON "Produk"("Merek_ID");
CREATE INDEX "idx_produk_model" ON "Produk"("Model_ID");
CREATE INDEX "idx_produk_jenis_body" ON "Produk"("JenisBody_ID");
CREATE INDEX "idx_produk_tahun_pembuatan" ON "Produk"("TahunPembuatan");

-- Tabel Iklan
CREATE TABLE "Iklan" (
    "ID" SERIAL PRIMARY KEY,
    "Pengguna_ID" INT NOT NULL,
    "Produk_ID" INT NOT NULL,
    "Judul" VARCHAR(255) NOT NULL,
    "Deskripsi" TEXT NOT NULL,
    "KontakPenjual" VARCHAR(255) NOT NULL,
    "IzinkanBid" BOOLEAN NOT NULL DEFAULT FALSE,
    "Catatan" TEXT,
    FOREIGN KEY ("Pengguna_ID") REFERENCES "Pengguna"("ID"),
    FOREIGN KEY ("Produk_ID") REFERENCES "Produk"("ID")
);

-- Menambahkan indeks pada foreign key di tabel Iklan
CREATE INDEX "idx_iklan_pengguna" ON "Iklan"("Pengguna_ID");
CREATE INDEX "idx_iklan_produk" ON "Iklan"("Produk_ID");

-- Tabel Bid
CREATE TABLE "Bid" (
    "ID" SERIAL PRIMARY KEY,
    "Iklan_ID" INT NOT NULL,
    "Pengguna_ID" INT NOT NULL,
    "Harga" DECIMAL(15,2) NOT NULL CHECK ("Harga" > 0),
    "Tanggal" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "Status" VARCHAR(255) CHECK ("Status" IN ('Pending', 'Diterima', 'Ditolak')) NOT NULL DEFAULT 'Pending',
    FOREIGN KEY ("Iklan_ID") REFERENCES "Iklan"("ID"),
    FOREIGN KEY ("Pengguna_ID") REFERENCES "Pengguna"("ID")
);

-- Menambahkan indeks pada foreign key di tabel Bid
CREATE INDEX "idx_bid_iklan" ON "Bid"("Iklan_ID");
CREATE INDEX "idx_bid_pengguna" ON "Bid"("Pengguna_ID");

-- Tabel Review
CREATE TABLE "Review" (
    "ID" SERIAL PRIMARY KEY,
    "Pengguna_ID" INT NOT NULL,
    "Penjual_ID" INT NOT NULL,
    "Rating" SMALLINT NOT NULL CHECK ("Rating" >= 1 AND "Rating" <= 5),
    "Komentar" TEXT,
    "Tanggal" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY ("Pengguna_ID") REFERENCES "Pengguna"("ID"),
    FOREIGN KEY ("Penjual_ID") REFERENCES "Pengguna"("ID")
);

-- Menambahkan indeks pada foreign key di tabel Review
CREATE INDEX "idx_review_pengguna" ON "Review"("Pengguna_ID");
CREATE INDEX "idx_review_penjual" ON "Review"("Penjual_ID");

-- Tabel Wishlist
CREATE TABLE "Wishlist" (
    "ID" SERIAL PRIMARY KEY,
    "Pengguna_ID" INT NOT NULL,
    "Produk_ID" INT NOT NULL,
    UNIQUE ("Pengguna_ID", "Produk_ID"),
    FOREIGN KEY ("Pengguna_ID") REFERENCES "Pengguna"("ID"),
    FOREIGN KEY ("Produk_ID") REFERENCES "Produk"("ID")
);

-- Menambahkan indeks pada foreign key di tabel Wishlist
CREATE INDEX "idx_wishlist_pengguna" ON "Wishlist"("Pengguna_ID");
CREATE INDEX "idx_wishlist_produk" ON "Wishlist"("Produk_ID");

-- Tabel RiwayatBid
CREATE TABLE "RiwayatBid" (
    "ID" SERIAL PRIMARY KEY,
    "Bid_ID" INT NOT NULL,
    "UrutanBid" SMALLINT NOT NULL,
    "HargaBid" DECIMAL(15,2) NOT NULL CHECK ("HargaBid" > 0),
    "TanggalBid" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY ("Bid_ID") REFERENCES "Bid"("ID")
);

-- Menambahkan indeks pada foreign key di tabel RiwayatBid
CREATE INDEX "idx_riwayat_bid" ON "RiwayatBid"("Bid_ID");