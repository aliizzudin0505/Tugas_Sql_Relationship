import psycopg2
import pandas as pd


# Koneksi ke database PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="test",
    user="postgres",
    password="Izulganteng",
    port="5432"  # Port default PostgreSQL
)

cur = conn.cursor()

# Daftar file CSV dan tabel yang sesuai 
csv_files = {
    "penjualan_mobil_bekas_domisili.csv": "Domisili",
    "penjualan_mobil_bekas_merek.csv": "Merek",
    "penjualan_mobil_bekas_model.csv": "Model",
    "penjualan_mobil_bekas_jenis_body.csv": "JenisBody",
    "penjualan_mobil_bekas_pengguna.csv": "Pengguna",
    "penjualan_mobil_bekas_produk.csv": "Produk",
    "penjualan_mobil_bekas_iklan.csv": "Iklan",
    "penjualan_mobil_bekas_bid.csv": "Bid",
    "penjualan_mobil_bekas_review.csv": "Review",
    "penjualan_mobil_bekas_wishlist.csv": "Wishlist",
    "penjualan_mobil_bekas_riwayatbid.csv": "RiwayatBid"
}
schema_name = "public"

# Fungsi untuk mengimpor data dari CSV ke tabel dengan transaksi
def import_csv_to_table(csv_file, table_name):
    try:
        # Mulai transaksi
        cur.execute("BEGIN TRANSACTION")

        # Gunakan identifier quoting untuk nama skema dan tabel
        schema_name_quoted = psycopg2.extensions.quote_ident(schema_name, cur)
        table_name_quoted = psycopg2.extensions.quote_ident(table_name, cur)

        # Gunakan COPY untuk impor langsung dari file CSV
        with open(csv_file, 'r') as f:
            cur.copy_expert(f"COPY {schema_name_quoted}.{table_name_quoted} FROM STDIN WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',')", f)

        # Commit jika semua berhasil
        conn.commit()
        print(f"Data dari {csv_file} berhasil diimpor ke tabel {table_name}")

    except Exception as e:
        # Rollback jika terjadi error
        conn.rollback()
        print(f"Error saat mengimpor {csv_file}: {e}")

# Mengimpor data dari setiap file CSV 
for csv_file, table_name in csv_files.items():
    import_csv_to_table(csv_file, table_name)

# Menutup koneksi 
cur.close()
conn.close()