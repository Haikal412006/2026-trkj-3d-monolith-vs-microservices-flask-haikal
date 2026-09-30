# Mengimpor Flask untuk membuat aplikasi web/API
# jsonify digunakan untuk mengubah data Python menjadi JSON
# request digunakan untuk mengambil data yang dikirim oleh client
from flask import Flask, jsonify, request


# Membuat aplikasi Flask
app = Flask(__name__)


# Database bohongan (In-memory)
# Data hanya disimpan sementara di dalam program
# Data akan hilang ketika server dihentikan
books = [
    {
        # ID unik dari buku
        "id": 1,

        # Nama atau judul buku
        "title": "Belajar Flask",

        # Jumlah stok buku yang tersedia
        "stock": 5
    }
]


# List untuk menyimpan data pesanan
# Data order juga hanya disimpan sementara
orders = []


# =========================
# FITUR BUKU
# =========================

# Membuat endpoint untuk mengambil semua data buku
# URL: /books
# Method: GET
@app.route('/books', methods=['GET'])
def get_books():

    # Mengembalikan seluruh data buku
    # dalam format JSON
    return jsonify(books)


# =========================
# FITUR PESANAN
# =========================

# Membuat endpoint untuk membuat pesanan baru
# URL: /orders
# Method: POST
@app.route('/orders', methods=['POST'])
def create_order():

    # Mengambil data JSON yang dikirim oleh client
    data = request.get_json()

    # Mengambil nilai book_id dari data yang dikirim
    book_id = data.get('book_id')


    # Cek stok buku
    # Melakukan perulangan pada seluruh data buku
    for b in books:

        # Mengecek apakah ID buku sesuai
        # dan stok buku masih lebih dari 0
        if b['id'] == book_id and b['stock'] > 0:

            # Mengurangi stok buku sebanyak 1
            # karena buku berhasil dipesan
            b['stock'] -= 1


            # Membuat data pesanan baru
            order = {
                # Membuat ID pesanan berdasarkan
                # jumlah order yang sudah ada
                "id": len(orders) + 1,

                # Menyimpan ID buku yang dipesan
                "book_id": book_id,

                # Menentukan status pesanan
                "status": "berhasil"
            }


            # Menambahkan data pesanan
            # ke dalam list orders
            orders.append(order)


            # Mengembalikan data pesanan dalam JSON
            # dengan status HTTP 201 (Created)
            return jsonify(order), 201


    # Jika buku tidak ditemukan atau stok sudah habis,
    # maka mengembalikan pesan error
    # dengan status HTTP 400 (Bad Request)
    return jsonify({
        "error": "Buku tidak ditemukan atau stok habis"
    }), 400


# =========================
# MENJALANKAN SERVER
# =========================

# Mengecek apakah program dijalankan secara langsung
if __name__ == '__main__':

    # Menjalankan server Flask pada port 5000
    # debug=True digunakan agar perubahan kode
    # dapat langsung terdeteksi saat pengembangan
    app.run(port=5000, debug=True)