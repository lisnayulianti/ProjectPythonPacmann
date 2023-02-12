import pandas as pd

"""
mengimpor pandas untuk mempermudah pekerjaan dengan lybrary python yang tersedia
"""

class Transaction:
  def __init__(self):
    """
    Inisialisasi kelas dan atributnya
    """

    self.daftar_transaksi=list()
  
  def add_item(self):
    """
    Membuat method tambah barang yang bernama add_item. Yang terdiri atas:
    nama_item: nama barang yang akan dibeli, tipe data: string
    jumlah_item: jumlah barang yang akan dibeli, tipe data integer
    harga_item: harga satuan dari barang yang kan dibeli, tipe data integer
    total_harga: perkalian dari jumlah item yang dibeli dengan harganya

    Keempat variabel ini akan disimpan dalam list
    """
    try: #menggunakan try-except untuk menghindari TypeError saat input data
      nama_item=str(input("Masukkan barang yang ingin dibeli: "))
    except TypeError:
      print("Harus berupa kata atau string")
    try:
      jumlah_item=int(input("Masukkan jumlah barang yang dibeli "))
    except TypeError:
      print("Harus berupa angka")
    try:
      harga_item=int(input("Masukkan harga per item "))
    except TypeError:
      print("Harus berupa angka")
    total_harga=jumlah_item*harga_item
    self.daftar_transaksi.append([nama_item, jumlah_item, harga_item, total_harga])
    print("Tambah belanjaan berhasil")

  def check_order(self):
    """
    Membuat method cek order untuk mengecek kembali barang yang telah dimasukkan. Kemudian list belanjaan akan divisualkan dengan pandas dataframe
    """
    if(len(self.daftar_transaksi) == 0): #mengecek apakah sudah memasukkan daftar transaksi
      print("Daftar belanja masih kosong")
    else:
      data=pd.DataFrame(self.daftar_transaksi) #menginput data transaksi dalam pandas dataframe
      data.columns=['Barang yg Ingin dibeli', 'Jumlah Barang', 'Harga Satuan', 'Total']
      print(data.to_markdown())

"""
Ketiga method di bawah ini dibuat untuk memudahkan update daftar belanjaan baik dari nama barang, jumlah, maupun harga barangnya.
Pengecekan barang menggunakan index list untuk mengganti barang sesuai keinginan
"""

  def update_barang(self, nama_item, new_nama_item):
    self.daftar_transaksi[self.index_belanja(nama_item)][0]=new_nama_item
    print("Sukses update data!")
  
  def update_jumlah(self, nama_item, new_jumlah_item):
    self.daftar_transaksi[self.index_belanja(nama_item)][1]=new_jumlah_item
    print("Sukses update data!")
  
  def update_harga(self, nama_item, new_harga_item):
    self.daftar_transaksi[self.index_belanja(nama_item)][2]=new_harga_item
    print("Sukses update data!")

  def index_belanja(self, nama_item):
    for i in range (len(self.daftar_transaksi)):
      if nama_item == self.daftar_transaksi[i][0]:
        return i

  """
  Membuat method delete item untuk mendelete daftar belanjaan yang telah masuk ke dalam list dengan menggunakan build in method list yang ada pada python
  """
  def delete_item(self, nama_item):
    self.daftar_transaksi.remove()
    print("Barang dihapus!")
 """
  Membuat method reset transaction untuk mendelete seluruh isi list daftar belanjaan yang telah masuk ke dalam list dengan menggunakan build in method list yang ada pada python
  """
  def reset_transaction(self):
    self.daftar_transaksi.clear()
    print("Data clear!")

"""
membuat method pembayaran untuk mengecek harga keseluruhan dari belanjaan yang telah dibeli
"""
  def pembayaran(self):
      total_keseluruhan = sum(self.daftar_transaksi[total_harga])
      if total_keseluruhan > 500000:
        print('Selamat! Anda mendapat diskon 10% sehingga total pembayaran anda adalah' + total_keseluruhan*0.9)
      elif total_keseluruhan > 300000 and total_keseluruhan < 500000:
        print('Selamat! Anda mendapat diskon 8% sehingga total pembayaran anda adalah' + total_keseluruhan*0.92)
      elif total_keseluruhan > 200000:
        print('Selamat! Anda mendapat diskon 5% sehingga total pembayaran anda adalah' + total_keseluruhan*0.95)
      else:
        print("Mohon maaf, anda belum mendapatkan diskon")