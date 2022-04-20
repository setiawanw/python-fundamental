"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""
# Sekuensial
print('Ibu berkata, "Pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telor beli 6"')
print('Maka Budi berangkat ke toko')
print('Dan mulai berbelanja')

# Percabangan
print("Tugas Budi")
berapa_botol_susu_yang_harus_dibeli = 1
butir_telur_yang_di_suruh_ibu = 6
print ("Stok di toko")
jumlah_botol_susu = 0
jumlah_telur = 6
print(f"Jumlah botol susu {jumlah_botol_susu} botol")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")  # Kapan-kapan dibikin lebih detil
else:
    print("Teryata habis")
print("Budi mengecek apakah ada telur?")
if jumlah_telur >= 6:
    print("Ternyata Ada")
else:
    print("Ternyata Habis")
if jumlah_telur >= 6 and jumlah_botol_susu > 0:
    print("Budi membeli 1 botol susu, dan 6 butir telur")
else:
    print(f"Budi membeli {berapa_botol_susu_yang_harus_dibeli} botol susu dan {butir_telur_yang_di_suruh_ibu} butir telur")
    # dua if diatas apakah memungkinkan tabrakan atau error
    # bagaimana membuat Budi hanya membeli susu
print("Budi pulang kerumah")
print("Budi meyerahkan hasil belanjanya kepada Ibu")
