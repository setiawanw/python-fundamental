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

daftar_buku = [1, 'kenji volume 2', -313, 3.14] #perhatikan, ada elemen yang pakai petik '' ada yang tidak
print('\nTampilkan dengan "for in range", dimana tipe data tiap elemen berbeda2')
for i in range(0, len(daftar_buku)): # kenapa i? i itu dipakai dari kebiasaan pemrograman lama dan len() adalah panjang suatu data
    print(daftar_buku[i])

print('Kembalikan nilai awal daftar_buku')
daftar_buku = ['Seven Habit', 'How to Influence People', 'First Things First', '40X']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Dunia Matematika Kelas 5')
for i in range(0, len(daftar_buku)): # kenapa i? i itu dipakai dari kebiasaan pemrograman lama dan len() adalah panjang suatu data
    print(daftar_buku[i])

# masuk materi Tipe Data List Part 2
print('\nClear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['Seven Habit', 'How to Influence People', 'First Things First', '40X']
daftar_buku[0] = 'Eight Habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


#print('\nBuku yang diambil tadi')
#print(buku)
#daftar_buku.pop() perintah ini bisa dipanggil tanpa menggunakan parameter, misal di bawah ini

print('\nBuku yang diambil tadi "tanpa perintah pop"')
print(buku)

print('\nPop "buku yang tersisa"')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nPop -1') #berguna jika bermain dengan Tipe Data Stack
daftar_buku = ['Seven Habit', 'How to Influence People', 'First Things First', '40X']
daftar_buku.pop(-1) # -1 berarti buku keempat '40X' akan hilang, -1 itu dihitung dari belakang
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# masuk materi Tipe Data List Comprehension (sudah di copas di module dasar_sintaksis_tipe_data_listcomprehension):
print('\nPerintah del')
daftar_buku = ['Seven Habit', 'How to Influence People', 'First Things First', '40X']
del daftar_buku[0] #0 berarti buku ke 1 'Seven Habit' akan hilang
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Seven Habit', 'How to Influence People', 'First Things First', '40X']
del daftar_buku[:] # [:] berarti hapus semua elemen -- aslinya [start:stop}
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

#print('\nPerintah del dengan list comprehension start:stop')
#daftar_buku = ['Seven Habit', 'How to Influence People', 'First Things First', '40X']
#del daftar_buku[0:3] # [0:3] hapus dari index 0 'Seven Habit', dan hapus sejumah 3 elemen, jadi nanti sisa 40X (index itu dihitung dari 0, sementara jumlah itu dari 1)
#for i in range(0, len(daftar_buku)):
#    print(daftar_buku[i])

#Coba ini:
#print('\nPerintah del dengan list comprehension start:stop')
#daftar_buku = ['Seven Habit', 'How to Influence People', 'First Things First', '40X']
#del daftar_buku[0:-2]
#for i in range(0, len(daftar_buku)):
#    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start:stop')
daftar_buku = ['Seven Habit', 'How to Influence People', 'First Things First', '40X']
del daftar_buku[0::2] #yang dihapus bisa di jeda2 -- slicing datafor i in range(0, len(daftar_buku)):
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
