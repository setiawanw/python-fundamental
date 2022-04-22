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

print('\nMembuat list baru')
daftar_buku = ['Seven Habit', 'How to Influence People', 'First Things First', '40X']
daftar_buku_baru = daftar_buku[:] #kalo tanpa [:] daftar_buku_baru akan disamakan dengan daftar_buku
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)): #len() nya sudah di isi range daftar_buku_baru
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension')
daftar_buku = ['Seven Habit', 'How to Influence People', 'First Things First', '40X']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)): #len() nya sudah di isi range daftar_buku_baru
    print(daftar_buku_baru[i])
#sampai menit ke 5.13
