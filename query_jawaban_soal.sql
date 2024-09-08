--Jawaban Nomer 4 a
SELECT * 
FROM "Produk"
WHERE "TahunPembuatan" >= 2015;

--Jawaban Nomer 4 b
INSERT INTO Bid (Iklan_ID, User_ID, Harga, Status)
VALUES (51, 3, 50000000, 'Pending');

--Jawaban Nomer 4 c
SELECT 
    P.*, 
    U."Nama" AS Nama_Penjual,
    P."Tanggal_Posting"
FROM 
    "Produk" P
JOIN 
    "Pengguna" U ON P."Penjual_ID" = U."ID"
WHERE 
    U."Role" = 'Penjual' 
    AND U."Nama" = 'Deborah Coleman' -- Ganti [Nama Penjual] dengan nama penjual yang diinginkan
ORDER BY 
    P."Tanggal_Posting" DESC;

--Jawaban Nomer 4 d
SELECT P.*
FROM "Produk" P
JOIN "Model" M ON P."Model_ID" = M."ID"
WHERE M."Nama" = 'Yaris'
ORDER BY P."Harga" ASC
LIMIT 10;

--Jawaban Nomer 4 e
SELECT 
    P.*, 
    D."Latitude" AS Domisili_Latitude, 
    D."Longitude" AS Domisili_Longitude,
    (6371 * acos(cos(radians(D."Latitude")) * cos(radians(D."Latitude")) * cos(radians(D."Longitude") - radians(D."Longitude")) + sin(radians(D."Latitude")) * sin(radians(D."Latitude")))) AS "Jarak"
FROM 
    "Produk" P
JOIN 
    "Pengguna" U ON P."Penjual_ID" = U."ID"
JOIN 
    "Domisili" D ON U."Domisili_ID" = D."ID"
WHERE 
    D."ID" = 20 AND P."Status" = 'Tersedia'
ORDER BY 
    "Jarak" ASC
LIMIT 1;


--Jawaban Nomer 5 a
SELECT 
    M."Nama" AS "Model_Mobil",
    (SELECT COUNT(DISTINCT "Model_ID") FROM "Produk") AS "Jumlah_Mobil",
    COUNT(B."ID") AS "Jumlah_Bid"
    
FROM 
    "Produk" P
JOIN 
    "Model" M ON P."Model_ID" = M."ID"
JOIN 
    "Iklan" I ON P."ID" = I."Produk_ID"
JOIN
    "Bid" B ON I."ID" = B."Iklan_ID"
GROUP BY 
    M."Nama"
ORDER BY 
    "Jumlah_Bid" DESC;

--Jawaban Nomer 5 b
SELECT 
    D."Kota",
    MR."Nama" AS "Merek",
    MO."Nama" AS "Model",
    P."TahunPembuatan",
    P."Harga",
    (SELECT AVG("Harga") FROM "Produk") AS "Rata_rata_Harga_Seluruh_Kota"
FROM 
    "Produk" P
JOIN 
    "Pengguna" U ON P."Penjual_ID" = U."ID"
JOIN
    "Domisili" D ON U."Domisili_ID" = D."ID"
JOIN
    "Merek" MR ON P."Merek_ID" = MR."ID"
JOIN
    "Model" MO ON P."Model_ID" = MO."ID";



--Jawaban Nomer 5 c
SELECT
	m."Nama" AS "NamaModel",
	u."Nama" AS "NamaUser",
	rb1."TanggalBid" AS "TanggalBidPertama",
	rb1."HargaBid" AS "HargaBidPertama",
	rb2."TanggalBid" AS "TanggalBidKedua",
	rb2."HargaBid" AS "HargaBidKedua"
FROM
"Produk" p
JOIN
"Model" m ON p."Model_ID" = m."ID"  -- Join ke tabel Model
JOIN
"Iklan" i ON p."ID" = i."Produk_ID"
JOIN
"Bid" b ON i."ID" = b."Iklan_ID"
JOIN
"Pengguna" u ON b."User_ID" = u."ID"
JOIN
"RiwayatBid" rb1 ON b."ID" = rb1."Bid_ID" AND rb1."UrutanBid" = 1
JOIN
"RiwayatBid" rb2 ON b."ID" = rb2."Bid_ID" AND rb2."UrutanBid" = 2
WHERE
p."Model_ID" = 1-- Ganti dengan ID model mobil yang diinginkan
    




--Jawaban Nomer 5 d
WITH "AvgBidPerModel" AS (
    SELECT 
        P."Model_ID", 
        AVG(B."Harga") AS "Rata2_Harga_Bid"
    FROM "Bid" B
    JOIN "Iklan" I ON B."Iklan_ID" = I."ID"
    JOIN "Produk" P ON I."Produk_ID" = P."ID"
    WHERE B."Tanggal" >= CURRENT_DATE - INTERVAL '6 MONTH' -- Perbaikan di sini
    GROUP BY P."Model_ID"
),

"AvgHargaMobilPerModel" AS (
    SELECT 
        P."Model_ID", 
        AVG(P."Harga") AS "Rata2_Harga_Mobil"
    FROM "Produk" P
    WHERE P."ID" IN (
        SELECT DISTINCT I."Produk_ID" 
        FROM "Iklan" I
        JOIN "Bid" B ON I."ID" = B."Iklan_ID"
        WHERE B."Tanggal" >= CURRENT_DATE - INTERVAL '6 MONTH' -- Perbaikan di sini
    )
    GROUP BY P."Model_ID"
)

SELECT 
    M."Nama" AS "Nama_Model",
    AB."Rata2_Harga_Bid",
    AM."Rata2_Harga_Mobil",
    AM."Rata2_Harga_Mobil" - AB."Rata2_Harga_Bid" AS "Diferrence",
    ((AM."Rata2_Harga_Mobil" - AB."Rata2_Harga_Bid") / AM."Rata2_Harga_Mobil") * 100 AS "Persentase_Perbedaan"
FROM "AvgBidPerModel" AB
JOIN "AvgHargaMobilPerModel" AM ON AB."Model_ID" = AM."Model_ID"
JOIN "Model" M ON AB."Model_ID" = M."ID";



--Jawaban Nomer 5 e
SELECT
    m."Nama" AS "Merek",
    mo."Nama" AS "Model",
    EXTRACT(MONTH FROM rb."TanggalBid") AS "Bulan", 
    EXTRACT(YEAR FROM rb."TanggalBid") AS "Tahun",
    AVG(rb."HargaBid") AS "RataRataHargaBid"
FROM
    "Produk" p
JOIN
    "Merek" m ON p."Merek_ID" = m."ID"
JOIN
    "Model" mo ON p."Model_ID" = mo."ID"
JOIN
    "Iklan" i ON p."ID" = i."Produk_ID"
JOIN
    "Bid" b ON i."ID" = b."Iklan_ID"
JOIN
    "RiwayatBid" rb ON b."ID" = rb."Bid_ID"
WHERE
    rb."TanggalBid" >= CURRENT_DATE - INTERVAL '6 MONTH' 
GROUP BY
    m."Nama",
    mo."Nama",
    EXTRACT(MONTH FROM rb."TanggalBid"),
    EXTRACT(YEAR FROM rb."TanggalBid")
ORDER BY
    m."Nama",
    mo."Nama",
    "Tahun",
    "Bulan";
