import csv
from datetime import datetime
import pytz

# CSV dosyasının yolu
dosya_yolu = 'domains.csv'

# Türkiye saat dilimi
turkey_tz = pytz.timezone('Europe/Istanbul')

# CSV dosyasını okuma ve işleme
with open(dosya_yolu, newline='') as csvfile:
    okuyucu = csv.reader(csvfile, delimiter='|')
    
    for satir in okuyucu:
        if len(satir) == 4:
            # Domain adını büyük harfe çevirme
            domain = satir[0].upper()
            
            # Başlangıç ve bitiş tarihlerini Türkiye saat diliminden UTC'ye çevirme
            baslangic_tarihi = turkey_tz.localize(datetime.strptime(satir[1], '%Y-%m-%d %H:%M')).astimezone(pytz.utc)
            bitis_tarihi = turkey_tz.localize(datetime.strptime(satir[2], '%Y-%m-%d %H:%M')).astimezone(pytz.utc)
            
            # Durumu 0 ve 1 olarak değiştirme
            durum = 1 if satir[3] == 'Aktif' else 0
            
            # Sonuçları ekrana bastırma
            print(f"Domain: {domain}, Başlangıç Tarihi (UTC): {baslangic_tarihi}, Bitiş Tarihi (UTC): {bitis_tarihi}, Durum: {durum}")
