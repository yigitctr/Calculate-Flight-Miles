def ucus_mili_hesapla(hiz, sure):
    # Hızı mil/saat cinsinden alıyoruz
    hiz_mil_saati = hiz * 0.621371

    # Uçuş süresini saat cinsinden alıyoruz
    sure_saat = sure / 60.0

    # Uçuş mili hesaplaması
    ucus_mili = hiz_mil_saati * sure_saat

    return ucus_mili

# Örnek: 500 km/saat hızla 2 saat uçuş
hiz = 500  # km/saat
sure = 2    # saat

sonuc = ucus_mili_hesapla(hiz, sure)
print(f"Uçuş Mili: {sonuc} mil")




#blackbox
# CTA sınıfını ve fonksiyonlarını tanımlama
class CTA:
    def __init__(self, miles):
        self.miles = miles

    def redeem_miles(self):
        return "Redeemed!"

# Kullanıcının sağladığı miles sayısı
user_miles = 10000

# Müşteri Temsilcisi (CTA) sınıfının bir örneğini oluşturma
cta = CTA(user_miles)

# Kazanılan mil leri kullanarak rezervasyon oluşturma
result = cta.redeem_miles()
print(result)