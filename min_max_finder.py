# Fonksiyon tanımlıyoruz.
def min_max_finder(numbers):
    en_kucuk = min(numbers)
    en_buyuk = max(numbers)
    return en_kucuk, en_buyuk

# Kullanıcıdan 5 adet tam sayı alıyoruz.
sayilar = []
for i in range(5):
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    sayilar.append(sayi)

# Fonksiyonu çağırıp ve sonucu ekrana yazdırıyoruz.
min_sayi, max_sayi = min_max_finder(sayilar)
print(f"Girilen sayıların en küçüğü: {min_sayi}")
print(f"Girilen sayıların en büyüğü: {max_sayi}")
