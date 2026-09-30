# Mengimpor Flask untuk membuat aplikasi web/API
# jsonify digunakan untuk mengubah data Python menjadi JSON
# request digunakan untuk mengambil data yang dikirim oleh client
from flask import Flask, jsonify, request

# Mengimpor library requests untuk melakukan komunikasi
# atau request HTTP ke Book Service
import requests


# Membuat aplikasi Flask
app = Flask(__name__)


# List untuk menyimpan data order sementara
# Data akan hilang jika aplikasi dihentikan
orders = []


# Alamat Book Service
# Book Service berjalan pada port 5001
BOOK_SERVICE_URL = "http://localhost:5001"


# Membuat endpoint untuk membuat order baru
# URL yang digunakan: /orders
# Method yang digunakan: POST
@app.route('/orders', methods=['POST'])
def create_order():

    # Mengambil data JSON yang dikirim oleh client
    data = request.get_json()

    # Mengambil nilai book_id dari data JSON
    book_id = data.get('book_id')


    # Komunikasi dengan Book Service
    try:

        # Mengirim request GET ke Book Service
        # untuk mengecek data buku berdasarkan book_id
        response = requests.get(
            f"{BOOK_SERVICE_URL}/books/{book_id}"
        )


        # Mengecek apakah Book Service berhasil
        # menemukan buku
        if response.status_code == 200:

            # Mengubah response JSON dari Book Service
            # menjadi data Python
            book_data = response.json()


            # Mengecek apakah stok buku masih tersedia
            if book_data['stock'] > 0:

                # Membuat data order baru
                order = {
                    # ID order dibuat berdasarkan jumlah
                    # data order yang sudah ada
                    "id": len(orders) + 1,

                    # Menyimpan ID buku yang dipesan
                    "book_id": book_id,

                    # Menentukan status order
                    "status": "berhasil"
                }


                # Menambahkan order ke dalam list orders
                orders.append(order)


                # Mengembalikan data order dalam format JSON
                # dengan status HTTP 201 (Created)
                return jsonify(order), 201


        # Jika buku tidak ditemukan atau stok tidak tersedia,
        # maka mengembalikan pesan error
        # dengan status HTTP 400 (Bad Request)
        return jsonify({
            "error": "Buku tidak tersedia"
        }), 400


    # Menangani error jika Book Service tidak dapat dihubungi
    except requests.exceptions.ConnectionError:

        # Mengembalikan pesan bahwa Book Service sedang down
        # dengan status HTTP 500 (Internal Server Error)
        return jsonify({
            "error": "Book Service sedang down!"
        }), 500


# Mengecek apakah file dijalankan secara langsung
if __name__ == '__main__':

    # Menjalankan aplikasi Order Service
    # pada port 5002
    # debug=True digunakan selama proses pengembangan
    app.run(port=5002, debug=True)