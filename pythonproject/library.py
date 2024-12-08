#Kütüphane Yönetim Sistemi
#bu proje kütüphane sistemini modellemiştir.

#kitap sınıfı:
#kitap adı,yazar adı,odünç alınma bilgilerini tutar.

#kütüphane sınıfı:
#kitap ekleme,ödünç verme,geri alma , mevcut kitapları ve ödünç kitapları listeleme gibi işlemleri gerçekleştirir.






class Kitap:
    def __init__(self,ad,yazar):
        self.ad = ad 
        self.yazar = yazar 
        self.oduncalindi = False

    def oduncver(self):
        if not self.oduncalindi:
            self.oduncalindi = True
    
    def gerial(self):
        if self.oduncalindi:
            self.oduncalindi = False
            
    def __str__(self):
        durum = "odunc Alindi" if self.oduncalindi else "mevcut"
        return f"{self.ad} - {self.yazar}({durum})"
    
class kutuphane:
    def __init__(self):
        self.kitaplar = []
        self.odunckitaplar = []

    def kitapekle(self,ad,yazar):
        yeni_kitap = Kitap(ad,yazar)
        self.kitaplar.append(yeni_kitap)
    
    def kitapoduncver(self,ad):
        for kitap in self.kitaplar:
            if kitap.ad == ad and not kitap.oduncalindi:
                if kitap.oduncver():
                    self.odunckitaplar.append(kitap)
                   
        
    def kitapgerial(self,ad):
        for kitap in self.odunckitaplar:
            if kitap.ad == ad:
                if kitap.gerial():
                    self.odunckitaplar.remove(kitap)
    
    def mevcutkitaplarilistele(self):
        print("mevcut kitaplar")
        for kitap in self.kitaplar:
            if not kitap.oduncalindi:
                print(kitap)


    def odunckitaplarilistele(self):
        print("odunc alinan kitaplar")
        for kitap in self.odunckitaplar:
            print(kitap)

if __name__ == "__main__":
    kutuphane = kutuphane()

    while True:
        print("1.Kitap Ekle")
        print("2.mevcut kitaplari listele")
        print("3.Odunç Kitaplari Listele")
        print("4.Kitap Odunç Ver")
        print("5.Kitap Geri Al")
        print("6.Cikis")

        secim = input("bir secim yapin")

        if secim == "1":
            ad = input("kitap adi")
            yazar = input("yazar adi")
            kutuphane.kitapekle(ad,yazar)
            print("kitap basariyla eklendi")
        elif secim == "2":
            kutuphane.mevcutkitaplarilistele()
        elif secim == "3":
            kutuphane.odunckitaplarilistele()
        elif secim =="4":
            ad = input("Odunç Verilecek Kitap Adi")
            if kutuphane.kitapoduncver(ad):
                print("kitap odunc verildi")
            else:
                print("kitap bulunamadi")
        elif secim =="5":
            ad = input("geri alinacak kitap")
            if kutuphane.kitapgerial(ad):
                print("kitap geri alindi")
            else:
                print("kitap bulunamadi")
        elif secim == "6":
            print("cikis yapiliyor")