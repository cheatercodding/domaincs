
import csv

# CSV dosyasının yolu
dosya_yolu = 'domains.csv'

# CSV dosyasını okuma ve içeriği ekrana yazdırma
with open(dosya_yolu, newline='') as csvfile:
    okuyucu = csv.reader(csvfile, delimiter='|')
    for satir in okuyucu:
        print(f"Satır: {satir}")  # Satırın tam içeriğini yazdır

       # Satırda 4 sütun olup olmadığını kontrol et
        if len(satir) == 4:
            print(f"Domain: {satir[0]}, Başlangıç Tarihi: {satir[1]}, Bitiş Tarihi: {satir[2]}, Durum: {satir[3]}")
        else:
            print(f"Geçersiz veya eksik bilgi içeren satır: {satir}")
