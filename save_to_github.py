import requests
import base64

# Ganti dengan informasi Anda
GITHUB_USERNAME = 'aliizzudin0505'
GITHUB_REPO = 'Tugas_Sql_Relationship'
GITHUB_TOKEN = 'xxxxxxx'

# Daftar file CSV dan path-nya di repositori GitHub
files_to_upload = {
    "penjualan_mobil_bekas_domisili.csv": "Domisili.csv",
    "penjualan_mobil_bekas_merek.csv": "Merek.csv",
    "penjualan_mobil_bekas_model.csv": "Model.csv",
    "penjualan_mobil_bekas_jenis_body.csv": "JenisBody.csv",
    "penjualan_mobil_bekas_pengguna.csv": "Pengguna.csv",
    "penjualan_mobil_bekas_produk.csv": "Produk.csv",
    "penjualan_mobil_bekas_iklan.csv": "Iklan.csv",
    "penjualan_mobil_bekas_bid.csv": "Bid.csv",
    "penjualan_mobil_bekas_review.csv": "Review.csv",
    "penjualan_mobil_bekas_wishlist.csv": "Wishlist.csv",
    "penjualan_mobil_bekas_riwayatbid.csv": "RiwayatBid.csv",
    "main_dummy.py" : "main.py",
    "postgresql_connector_main.py" : "connector.py",
    "query_main_database_postgresql.sql" : "main_database.sql",
    "query_pertanyaan.sql" : "query_jawaban_soal.sql",
    "Final Project - Relational Database.pdf" : "Permasalahan.pdf"
    
    
}

# Fungsi untuk mengupload file
def upload_file(file_path, github_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode('utf-8')

    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }

    url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{GITHUB_REPO}/contents/{github_path}'

    # Cek apakah file sudah ada
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        sha = response.json()['sha']
        data = {
            'message': 'Update file',
            'content': encoded_content,
            'sha': sha
        }
    else:
        data = {
            'message': 'Create file',
            'content': encoded_content
        }

    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 201 or response.status_code == 200:
        print(f'File {file_path} berhasil diupload ke {github_path}')
    else:
        print(f'Error mengupload file {file_path}: {response.json()}')

# Upload semua file
for file_name, github_path in files_to_upload.items():
    upload_file(file_name, github_path)
