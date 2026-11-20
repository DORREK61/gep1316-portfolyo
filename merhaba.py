# merhaba.py - GEP1316 Ödev 2
# Kullanıcının adını ve doğum yılını alıp yaşını hesaplayan,
# kişiye özel karşılama mesajı yazan ilk programım.

from datetime import date  # Bugünün tarihini almak için date sınıfını içeri aktarıyoruz

# input() kullanıcıdan klavyeyle bir metin (str) alır
ad = input("Adınız nedir? ")

# input() her zaman metin döndürür; int() bu metni tam sayıya çevirir
dogum_yili = int(input("Doğum yılınız kaç? "))

# Bu yılı otomatik alıyoruz, böylece program her yıl doğru çalışır
bu_yil = date.today().year

# Görev 4 - Geliştirme: doğum yılı gelecekteyse uyarı ver
if dogum_yili > bu_yil:
    print(f"Uyarı: {dogum_yili} henüz gelmedi! Lütfen geçerli bir doğum yılı girin.")
else:
    # Yaşı bulmak için bu yıldan doğum yılını çıkarıyoruz
    yas = bu_yil - dogum_yili

    # f-string ile değişkenleri cümlenin içine yerleştirip ekrana yazdırıyoruz
    print(f"Merhaba {ad}! Kodlama dünyasına hoş geldin.")
    print(f"{bu_yil} yılında {yas} yaşındasın (ya da bu yıl {yas} yaşına gireceksin).")
