import time

fiyatlar = {
  "1":1,
  "2":2,
  "3":3,
  "4":5,
  "5":7,
  "6":11,
}

urunler = {
  "1":"su",
  "2":"çay",
  "3":"kahve",
  "4":"enerji içeceği",
  "5":"paket portakal suyu",
  "6":"taze portakal suyu",
}
def sonsuz_girdi(mesaj, beklenen):
    while True:
        girdi = input(mesaj)
        if girdi in beklenen:
            return girdi
        else:
            print("Bir hata var burada")

def sayisal_sonsuz_girdi(mesaj):
    while True:
        girdi = input(mesaj)
        if girdi.isdigit():
            return int(girdi)
        else:
            print("Bir hata var burada")

def karsilama():  
    print("Hoşgeldiniz")
    print("Ürünler:")
    for anahtar, deger in urunler.items():
        print(anahtar, "|", deger) 

def veda():
    print("Tekrar bekleriz")
    time.sleep(2)
    print("\n"*23)

while True:
    karsilama()
    para_girdi = sayisal_sonsuz_girdi("Lütfen Para giriniz: ")
    urun_girdi = sonsuz_girdi("Ürün Seçiniz: ", urunler)
    fiyat = fiyatlar[urun_girdi]
    urun = urunler[urun_girdi]
    if fiyat > para_girdi:
        print("Paranız yetesiz geldiğinden iade edilmiştir", para_girdi)
    else:
        print("Ürününüzü Alınız", urun)
        print("Para Üstü", para_girdi - fiyat)
    veda()    

