# hesaplayici.py - GEP1316 Ödev 3
# Oyun Karakteri DPS (Saniye Başına Hasar) Hesaplayıcı
# Formül (beklenen değer):
#   DPS = hasar × saldırı_hızı × (1 + kritik_şans × (kritik_çarpan − 1))
# Burada kritik_şans 0 ile 1 arasında bir orandır (ör. %25 -> 0.25).

# --- Girdiler (input) ---
karakter_adi = input("Karakter adı: ")                      # str: metin
hasar = int(input("Vuruş başına hasar (tam sayı): "))       # int: tam sayı
saldiri_hizi = float(input("Saniyedeki saldırı sayısı: "))  # float: ondalıklı sayı

# Kritik vuruş özelliği var mı? Cevabı bool (True/False) değerine çeviriyoruz
kritik_cevap = input("Karakterin kritik vuruşu var mı? (e/h): ")
kritik_var = kritik_cevap.strip().lower() == "e"            # bool: True ya da False

if kritik_var:
    # Kullanıcı yüzde girer (ör. 25), biz bunu orana çeviriyoruz (0.25)
    kritik_yuzde = int(input("Kritik vuruş şansı (%): "))
    kritik_sans = kritik_yuzde / 100
    kritik_carpan = float(input("Kritik hasar çarpanı (ör. 2): "))
else:
    # Kritik yoksa formülde etkisi olmasın diye şans 0 olur
    kritik_sans = 0
    kritik_carpan = 1.0

# --- Hesaplama (aritmetik operatörler: *, +, -) ---
temel_dps = hasar * saldiri_hizi
dps = temel_dps * (1 + kritik_sans * (kritik_carpan - 1))

# --- Sınıflandırma (karşılaştırma operatörleri: >=, <) ---
if dps >= 200:
    seviye = "Boss seviyesi"
elif dps >= 100:
    seviye = "Güçlü"
elif dps >= 50:
    seviye = "Dengeli"
else:
    seviye = "Zayıf"

# --- Çıktı (f-string ile biçimlendirme, .2f = virgülden sonra 2 basamak) ---
print(f"\n{karakter_adi} için sonuçlar")
print(f"Temel DPS : {temel_dps:.2f}")
print(f"Toplam DPS: {dps:.2f}")
print(f"Seviye    : {seviye}")
print(f"Kritik vuruş aktif mi? {kritik_var}")
