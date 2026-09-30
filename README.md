# Praktikum Monolith dan Microservices
<div align="justify">
Project ini merupakan implementasi sederhana **Monolith** dan
**Microservices** menggunakan Python Flask.

## Struktur Project

``` text
MONOLITH_MICROSERVICES/
│
├── microservices/
│   ├── book_service.py
│   └── order_service.py
│
└── monolith/
    └── monolith_app.py
```

## 1. Persiapan

Pastikan Python sudah terinstall.

Cek versi Python:

``` bash
python --version
```

Install library yang dibutuhkan:

``` bash
pip install flask requests
```

**Hasil:** Flask dan Requests berhasil diinstall.

------------------------------------------------------------------------

## 2. Menjalankan Monolith

Jalankan perintah:

``` bash
python monolith/monolith_app.py
```

**Hasil:**

``` text
http://localhost:5000
```

### Cek Data Buku

Buka Postman, kemudian gunakan:

``` text
GET http://localhost:5000/books
```

**Hasil:** Data buku berhasil ditampilkan.

### Membuat Order

Gunakan:

``` text
POST http://localhost:5000/orders
```

Body → **raw → JSON**:

``` json
{
    "book_id": 1
}
```

**Hasil:**

``` json
{
    "id": 1,
    "book_id": 1,
    "status": "berhasil"
}
```

------------------------------------------------------------------------

## 3. Menjalankan Book Service

Buka **terminal baru**, kemudian jalankan:

``` bash
python microservices/book_service.py
```

**Hasil:**

``` text
http://localhost:5001
```

Cek menggunakan Postman:

``` text
GET http://localhost:5001/books
```

**Hasil:** Data buku berhasil ditampilkan.

------------------------------------------------------------------------

## 4. Menjalankan Order Service

Buka **terminal baru**, kemudian jalankan:

``` bash
python microservices/order_service.py
```

**Hasil:**

``` text
http://localhost:5002
```

### Membuat Order

Gunakan Postman:

``` text
POST http://localhost:5002/orders
```

Body → **raw → JSON**:

``` json
{
    "book_id": 1
}
```

**Hasil:**

``` json
{
    "id": 1,
    "book_id": 1,
    "status": "berhasil"
}
```

------------------------------------------------------------------------

## 5. Pengujian

Untuk menguji komunikasi antar-service, hentikan **Book Service**
dengan:

``` text
CTRL + C
```

Kemudian coba membuat order kembali:

``` text
POST http://localhost:5002/orders
```

**Hasil:**

``` json
{
    "error": "Book Service sedang down!"
}
```

------------------------------------------------------------------------

## 6. Port yang Digunakan

  Service           Port
  --------------- ------
  Monolith          5000 
  Book Service      5001
  Order Service     5002

## 7. Kesimpulan
<div align="justify">

Berdasarkan praktikum yang telah dilakukan, **Monolith** menjalankan fitur buku dan order dalam satu aplikasi pada port `5000`.

Sedangkan **Microservices** memisahkan aplikasi menjadi **Book Service** pada port `5001` dan **Order Service** pada port `5002`. Kedua service dapat berkomunikasi menggunakan HTTP.

Dari hasil pengujian, kedua arsitektur berhasil dijalankan dan fungsi pemesanan dapat diuji melalui REST API.
