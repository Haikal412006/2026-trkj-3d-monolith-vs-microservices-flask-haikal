# Mengimpor Flask untuk membuat aplikasi web/API
# dan jsonify untuk mengubah data Python menjadi format JSON
from flask import Flask, jsonify

# Membuat objek aplikasi Flask
app = Flask(__name__)


# Database sederhana khusus untuk Book Service
# Data disimpan sementara dalam bentuk list
books = [
    {
        # ID unik untuk setiap buku
        "id": 1,

        # Judul buku
        "title": "Belajar Flask",

        # Jumlah stok buku yang tersedia
        "stock": 5
    }
]


# Route untuk mengambil semua data buku
# URL yang digunakan: /books
# Method yang digunakan: GET
@app.route('/books', methods=['GET'])
def get_books():

    # Mengembalikan seluruh data books dalam format JSON
    return jsonify(books)


# Route untuk mengambil satu data buku berdasarkan ID
# Contoh URL: /books/1
# Method yang digunakan: GET
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):

    # Melakukan perulangan untuk mencari buku
    # berdasarkan ID yang diberikan pada URL
    for b in books:

        # Mengecek apakah ID buku sama dengan book_id
        if b['id'] == book_id:

            # Jika ditemukan, data buku dikembalikan
            # dalam format JSON
            return jsonify(b)

    # Jika buku dengan ID tersebut tidak ditemukan,
    # maka mengembalikan pesan error
    # dengan status HTTP 404 (Not Found)
    return jsonify({
        "error": "Not found"
    }), 404


# Menjalankan aplikasi Flask
# Bagian ini hanya dijalankan ketika file
# dijalankan secara langsung
if __name__ == '__main__':

    # Menjalankan server Flask pada port 5001
    # debug=True digunakan agar perubahan kode
    # dapat langsung terdeteksi saat pengembangan
    app.run(port=5001, debug=True)