daftar_buku = ['Seven Habit', 'How to Influence People', 'First Things First', '40X']
print('\nTampikan variabel daftar_buku')
print(daftar_buku)

print('\nProses semua dengan "for in"')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan "for in range"')
for i in range(0, len(daftar_buku)): # kenapa i? i itu dipakai dari kebiasaan pemrograman lama dan len() adalah panjang suatu data
    print(daftar_buku[i])

daftar_buku = [1, 'kenji volume 2', -313, 3.14] #perhatikan, ada data yang pakai petik '' ada yang tidak
print('\nTampilkan dengan "for in range", dimana tipe data tiap elemen berbeda2')
for i in range(0, len(daftar_buku)): # kenapa i? i itu dipakai dari kebiasaan pemrograman lama dan len() adalah panjang suatu data
    print(daftar_buku[i])

print('Kembalikan nilai awal daftar_buku')
daftar_buku = ['Seven Habit', 'How to Influence People', 'First Things First', '40X']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Dunia Matematika Kelas 5')
for i in range(0, len(daftar_buku)): # kenapa i? i itu dipakai dari kebiasaan pemrograman lama dan len() adalah panjang suatu data
    print(daftar_buku[i])

