# Final Project Pacmann - Self Service Cashier

Self Service Cashier sederhana yang dibuat menggunakan bahasa pemrograman python

# Objective

Pada project kali ini, saya diminta untuk membuat sebuah program self service cashier untuk membantu perbaikan proses bisnis sebuah minimarket. Diharapkan dengan software
self service cashier ini, customer bisa langsung memasukkan barang belanjaannya. Kemudahan ini juga berpotensi untuk memperluas jangkauan minimarket dalam mencari
konsumen baru karena customer tidak perlu berada di minimarket tersebut untuk berbelanja.

Adapun requirement dari software ini adalah:
1. Customer dapat memasukkan item yang ingin dibeli berupa nama barang, jumlah dan harga satuan barang tersebut
2. Customer dapat mengubah list pemesanan barang baik itu nama barang, jumlah, dan harga satuannya
3. Customer dapat membatalkan pesanan, baik untuk barang tertentu maupun keseluruhan list belanjanya
4. Customer dapat mengecek kembali pesanan barang yang telah dilakukan
5. Customer dapat menghitung total barang beserta potongan barang ketika ada syarat tertentu

# Flowchart dari Program Cashier
Berikut ini merupakan flowchart dari program self service cashier

![Untitled Diagram](https://user-images.githubusercontent.com/55594639/218298691-b0efbc91-6670-412a-9014-ef939b53ecd2.jpg)
Pertama, customer akan membuat ID Transaksi. Kemudian customer melakukan input data barang yang akan dibeli. Setelah diinput, customer melakukan pengecekan. Apabila ada dat yang perlu diperbaiki, maka customer akan menggunkanan fitur update untuk memperbaiki. Setelah semua sudah benar, maka akan lanjut ke pembayaran

# Function dan atrribut yang dibuat beserta fungsinya
Fungsi yang dibuat antara lain:
1. Fungsi add_item, digunakan untuk menambahkan barang yang akan dibeli. Terdiri atas 4 variabel yaitu 
    a. nama_item, berupa string yang merupakan nama barang yang akan dibeli
    b. jumlah_item, berupa integer yang merupakan jumlah barang yang akan dibeli
    c. harga_item, berupa integer yang merupakan harga satuan dari barang tersebut
    d. total_harga, berupa integer dan merupakan hasil perkalian antara jumlah barang dengan harga
2. check_order, digunakan untuk mengecek data yang telah diinput dan kemudian dimasukkan ke dalam pandas dataframe agar lebih rapih
3. Update_barang, update_jumlah, update+harga, merupakan fungsi untuk mengupdate data apabila ada kesalahan dalam proses input data
4. Delete_item, digunakan untuk menghapus barang yang telah ada di list belanjaan tetapi tidak jadi dibeli
5. reset_transaction, untuk menghapus seluruh list barang yang telah terinput
6. Pembayaran, untuk menghitung harga akhir setelah dikurangi diskon

# Test Case

Test case berhasil dijalankan di Google Colab. Namun, gagal dijalankan di terminal.

# Kesimpulan

Program self service cashier ini sudah berjalan baik ketika dijalankan di Google Colab. Namun sayangnya, belum berhasil dijalankan di terminal windows
