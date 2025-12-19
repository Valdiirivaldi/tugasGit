data_panen = {
    "lokasi1": {
        "nama_lokasi": "Kebun A",
        "hasil_panen": {
            "padi": 1200,
            "jagung": 800,
            "kedelai": 500
        }
    },
    "lokasi2": {
        "nama_lokasi": "Kebun B",
        "hasil_panen": {
            "padi": 1500,
            "jagung": 900,
            "kedelai": 450
        }
    },
    "lokasi3": {
        "nama_lokasi": "Kebun C",
        "hasil_panen": {
            "padi": 1100,
            "jagung": 750,
            "kedelai": 600
        }
    },
    "lokasi4": {
        "nama_lokasi": "Kebun D",
        "hasil_panen": {
            "padi": 1300,
            "jagung": 850,
            "kedelai": 550
        }
    },
    "lokasi5": {
        "nama_lokasi": "Kebun E",
        "hasil_panen": {
            "padi": 1400,
            "jagung": 950,
            "kedelai": 480
        }
    }
}

for lokasi, data in data_panen.items():
    print(lokasi)
    print("Nama Lokasi :", data["nama_lokasi"])
    print("Hasil Panen :", data["hasil_panen"])
    print()

print("2.	Tampilkan jumlah hasil panen jagung dari lokasi2.")
jagung_lokasi2 = data_panen["lokasi2"]["hasil_panen"]["jagung"]
print("Hasil panen jagung lokasi2:", jagung_lokasi2)

print("3.	Tampilkan nama lokasi dari lokasi3.")
nama_lokasi3 = data_panen["lokasi3"]["nama_lokasi"]
print("Nama lokasi3:", nama_lokasi3)


print("4 dan 5 Variabel terpisah hasil panen padi dan kedelai tiap lokasi")

padi_lokasi1 = data_panen["lokasi1"]["hasil_panen"]["padi"]
kedelai_lokasi1 = data_panen["lokasi1"]["hasil_panen"]["kedelai"]

padi_lokasi2 = data_panen["lokasi2"]["hasil_panen"]["padi"]
kedelai_lokasi2 = data_panen["lokasi2"]["hasil_panen"]["kedelai"]

padi_lokasi3 = data_panen["lokasi3"]["hasil_panen"]["padi"]
kedelai_lokasi3 = data_panen["lokasi3"]["hasil_panen"]["kedelai"]

padi_lokasi4 = data_panen["lokasi4"]["hasil_panen"]["padi"]
kedelai_lokasi4 = data_panen["lokasi4"]["hasil_panen"]["kedelai"]

padi_lokasi5 = data_panen["lokasi5"]["hasil_panen"]["padi"]
kedelai_lokasi5 = data_panen["lokasi5"]["hasil_panen"]["kedelai"]


print("Buat Percabangan")
for lokasi, data in data_panen.items():
    padi = data["hasil_panen"]["padi"]
    jagung = data["hasil_panen"]["jagung"]

    if padi > 1300 or jagung > 800:
        print(data["nama_lokasi"], "memerlukan perhatian khusus")
    else:
        print(data["nama_lokasi"], "dalam kondisi baik")

print("Update commit kedua")
print("pindah di branch Baru")
print("rubah  di master Baru")

