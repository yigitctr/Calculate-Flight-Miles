class HesaplaUcusMilesDetay:
    def __init__(self, musteri_kodu, istemci_kullanici_adi, kanal, havayolu_kodu, basvuru, 
                 client_transaction_id, dil_kodu):
        self.musteri_kodu = musteri_kodu
        self.istemci_kullanici_adi = istemci_kullanici_adi
        self.kanal = kanal
        self.havayolu_kodu = havayolu_kodu
        self.basvuru = basvuru
        self.client_transaction_id = client_transaction_id
        self.dil_kodu = dil_kodu

# Örnek kullanım:
ucus_detay = HesaplaUcusMilesDetay(
    musteri_kodu="123456",
    istemci_kullanici_adi="kullanici123",
    kanal="web",
    havayolu_kodu="TK",
    basvuru="Uçuş Hesaplama Uygulaması",
    client_transaction_id="trans123",
    dil_kodu="TR"
)

# Örnek detaylara erişim:
print(f"Müşteri Kodu: {ucus_detay.musteri_kodu}")
print(f"İstemci Kullanıcı Adı: {ucus_detay.istemci_kullanici_adi}")
print(f"Kanal: {ucus_detay.kanal}")
print(f"Havayolu Kodu: {ucus_detay.havayolu_kodu}")
print(f"Başvuru: {ucus_detay.basvuru}")
print(f"Client Transaction ID: {ucus_detay.client_transaction_id}")
print(f"Dil Kodu: {ucus_detay.dil_kodu}")

class UcusBilgisi:
    def __init__(self, mensi_havaalani_kodu, varis_havaalani_kodu, sinif_kodu, kabin_kodu, kart_tipi, ucus_tarihi):
        self.mensi_havaalani_kodu = mensi_havaalani_kodu
        self.varis_havaalani_kodu = varis_havaalani_kodu
        self.sinif_kodu = sinif_kodu
        self.kabin_kodu = kabin_kodu
        self.kart_tipi = kart_tipi
        self.ucus_tarihi = ucus_tarihi

# Örnek kullanım:
ucus_bilgisi = UcusBilgisi(
    mensi_havaalani_kodu="IST",
    varis_havaalani_kodu="JFK",
    sinif_kodu="Economy",
    kabin_kodu="Y",
    kart_tipi="CC",
    ucus_tarihi="01.12.2023"
)

# Örnek detaylara erişim:
print(f"Menşei Havaalanı Kodu: {ucus_bilgisi.mensi_havaalani_kodu}")
print(f"Varış Havaalanı Kodu: {ucus_bilgisi.varis_havaalani_kodu}")
print(f"Sınıf Kodu: {ucus_bilgisi.sinif_kodu}")
print(f"Kabin Kodu: {ucus_bilgisi.kabin_kodu}")
print(f"Kart Tipi: {ucus_bilgisi.kart_tipi}")
print(f"Uçuş Tarihi: {ucus_bilgisi.ucus_tarihi}")

class UcusSonucu:
    def __init__(self, sonuc_kodu, sonuc_aciklama, tanim, ucus_sayisi, base_miles, temel_nokta, promosyon_miles,
                 promosyon_puanlari, toplam_mil, kabin_tipi, sinif_kodlari):
        self.sonuc_kodu = sonuc_kodu
        self.sonuc_aciklama = sonuc_aciklama
        self.tanim = tanim
        self.ucus_sayisi = ucus_sayisi
        self.base_miles = base_miles
        self.temel_nokta = temel_nokta
        self.promosyon_miles = promosyon_miles
        self.promosyon_puanlari = promosyon_puanlari
        self.toplam_mil = toplam_mil
        self.kabin_tipi = kabin_tipi
        self.sinif_kodlari = sinif_kodlari

# Örnek kullanım:
ucus_sonucu = UcusSonucu(
    sonuc_kodu="ABC123",
    sonuc_aciklama="Başarılı",
    tanim="İstanbul-New York (Ekonomi : Y,B,S,G,H,L,M,Q,T,V,W,E,P,F)",
    ucus_sayisi="1",
    base_miles="500",
    temel_nokta="0",
    promosyon_miles="50",
    promosyon_puanlari="0",
    toplam_mil="550",
    kabin_tipi="Ekonomi",
    sinif_kodlari="Y,B,S,G,H,L,M,Q,T,V,W,E,P,F"
)

# Örnek detaylara erişim:
print(f"Sonuç Kodu: {ucus_sonucu.sonuc_kodu}")
print(f"Sonuç Açıklama: {ucus_sonucu.sonuc_aciklama}")
print(f"Tanim: {ucus_sonucu.tanim}")
print(f"Uçuş Sayısı: {ucus_sonucu.ucus_sayisi}")
print(f"Base Miles: {ucus_sonucu.base_miles}")
print(f"Temel Nokta: {ucus_sonucu.temel_nokta}")
print(f"Promosyon Miles: {ucus_sonucu.promosyon_miles}")
print(f"Promosyon Puanları: {ucus_sonucu.promosyon_puanlari}")
print(f"Toplam Mil: {ucus_sonucu.toplam_mil}")
print(f"Kabin Tipi: {ucus_sonucu.kabin_tipi}")
print(f"Sınıf Kodları: {ucus_sonucu.sinif_kodlari}")
