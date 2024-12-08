#Hava Durumu 

#Bu proje bir şehir için hava durumu tahmini yapar.

#Şehir Sınıfı:
#şehir adı (ad) ve sıcaklık bilgilerini(sicaklik) tutar.

#HavaDurumu Sınıfı:
#şehir ekleme(sehirekleme) , sıcaklık güncelleme(sicaklikgunceller) , hava durumu sorgulama(havadurumusorgulama) , sıcaklığa göre tavsiyeler (sıcaklıgagoretavsiye) verme işlemlerini gerçekleştirir.



class Sehir:
    def __init__(self,ad,sicaklik):
        self.ad = ad 
        self.sicaklik = sicaklik 

    def __str__(self):
        return f"{self.ad}:{self.sicaklik}°C"
    
class HavaDurumu:
    def __init__(self):
        self.sehirler = []

    def sehirekle(self,ad,sicaklik):
        yenisehir = Sehir(ad,sicaklik)
        self.sehirler.append(yenisehir)
    
    def sicaklikguncelle(self,ad,yenisicaklik):
        for sehir in self.sehirler:
            if sehir.ad == ad:
                sehir.sicaklik = yenisicaklik
                
        
    def havadurumusorgula(self,ad):
        for sehir in self.sehirler:
            if sehir.ad == ad:
                return True
            return False
    
    def sicakligagoretavsiye(self,sicaklik):
        if sicaklik < 0 :
            return "Hava Soğuk, dikkatli olun."
        elif 0 <= sicaklik <=15:
            return "Hava Serin,mont/ceket almayi unutmayin."
        else:
            return "Hava Sicak,İnce kiyafetler giyebilirsiniz. "
    
    def sehirlerlistele(self):
        print("Sehirler ve Sicakliklari:")
        for sehir in self.sehirler:
            print(sehir)

if __name__ == "__main__":
    havadurumu = HavaDurumu()

    while True:
        print("1.Sehir Ekle")
        print("2.Sicaklik Guncelle")
        print("3.Hava durumunu Sorgula")
        print("4.Sehirleri Listele")
        print("5.Cikis")

        secim = input("Bir secim yapin:")

        if secim == "1":
            ad = input ("Sehir Adi:")
            sicaklik = float(input("Sicaklik °C:"))
            havadurumu.sehirekle(ad,sicaklik)
            print("Sehir basariyla eklendi.")
        elif secim == "2":
            ad = input("sicakligi guncellenecek sehir:")
            yenisicaklik = float(input("Yeni Sicaklik °C"))
            if havadurumu.sicaklikguncelle(ad,yenisicaklik):
                print("sicaklik guncellendi.")
            else:
                print("Sehir bulunamadi")

        elif secim =="3":
            ad = input("hava durumu sorgulanacak sehir:")
            sehir = havadurumu.havadurumusorgula(ad)
            if sehir:
                print(sehir)
                print(havadurumu.sicakligagoretavsiye(sehir.sicaklik))
            else:
                print("Sehir Bulunamadi.")
        
        elif secim == "4":
            havadurumu.sehirlerlistele()
        
        elif secim == "5":
            print("Cikis Yapiliyor")
