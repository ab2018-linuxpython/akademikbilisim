#! /usr/bin/env python
import time
import sys

urunler = {
  "1":("su", 1),
  "2":("çay", 2),
  "3":("kahve", 3),
  "4":("enerji içeceği", 5),
  "5":("paket portakal suyu", 7),
  "6":("taze portakal suyu", 11),
}


def input(mesaj):
    sys.stdout.write(mesaj)
    sys.stdout.flush()
    girdiler = []
    while True:
        girdi = sys.stdin.read(1)
        if girdi == "\n":
            break
        else:
            girdiler.append(girdi)
    return "".join(girdiler)

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
    print("\n".join(karsilama_str()))
        
def karsilama_str():
    degerler = []
    degerler.append("Hoşgeldiniz")
    degerler.append("Ürünler:")
    for anahtar, deger in urunler.items():
        degerler.append(" ".join((anahtar, "|", str(deger))))
    return degerler
    
def veda():
    print("Tekrar bekleriz")
    time.sleep(2)
    print("\n"*23)


if __name__ == "__main__":
    import signal
    import argparse

    kasa = 0
    
    def _usr1_handler(signal, context):
        print("Kasa para:", kasa, file=sys.stderr, flush=True)
        
    signal.signal(signal.SIGUSR1, _usr1_handler)
    
    parser = argparse.ArgumentParser(description=' ## '.join(karsilama_str()+
                                                           ["", "Hata kodu 1 = yetersiz bakiye"]))
    parser.add_argument("-p", '--para',type=int, help='girilen para')
    parser.add_argument("-u", '--urun',type=int, help='istenen urun')
    
    if len(sys.argv) >1:
        argumanlar = parser.parse_args()
        urun_girdi = argumanlar.urun
        urun, fiyat = urunler[str(urun_girdi)]
        para_girdi = argumanlar.para
        if fiyat > para_girdi:
            exit(1)
        else:
            print("Ürününüzü Alınız", urun)
            print("Para Üstü", para_girdi - fiyat)
            exit()
    else:
        while True:
            karsilama()
            para_girdi = sayisal_sonsuz_girdi("Lütfen Para giriniz: ")
            urun_girdi = sonsuz_girdi("Ürün Seçiniz: ", urunler)
            urun, fiyat = urunler[urun_girdi]
            if fiyat > para_girdi:
                print("Paranız yetesiz geldiğinden iade edilmiştir", para_girdi)
            else:
                kasa += fiyat
                print("Ürününüzü Alınız", urun)
                print("Para Üstü", para_girdi - fiyat)
            veda()
