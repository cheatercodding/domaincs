

import csv

# CSV dosyasının yolu
dosya_yolu = 'domains.csv'

# CSV dosyasını okuma ve içeriği ekrana yazdırma
with open(dosya_yolu, newline='') as csvfile:
    okuyucu = csv.reader(csvfile, delimiter='|')
    for satir in okuyucu:
        print(f"Domain: {satir[0]}, Başlangıç Tarihi: {satir[1]}, Bitiş Tarihi: {satir[2]}, Durum: {satir[3]}")
