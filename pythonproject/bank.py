#Banka Sistemi
#Bu sistem Banka sistemindeki işlevleri yerine getirir.

#Kullanıcı sınıfı:
#ad (ad), hesap numarası(hesapno) , bakiye(bakiye) bilgilerini tutar.

#Banka sınıfı:
#hesap açma (hesapac), hesapno kontrolü (hesapno_varmi) , kullanıcı bulma (kullanıcıbul) , 
# para yatır (parayatir) , para çek (paracek) , bakiye sorgula (bakiyesorgula), kullanıcı listeleme (kullanicilisteleme) işlemlerini gerçekleştirir.


class Kullanici:
    def __init__(self,ad,hesapno,bakiye):
        self.ad = ad
        self.hesapno = hesapno
        self.bakiye = bakiye
    
    def parayatir(self,miktar):
        if miktar > 0:
            self.bakiye += miktar
    
    def paracek(self,miktar):
        if 0 < miktar <= self.bakiye:
            self.bakiye -= miktar
            
    def __str__(self):
        return f"Ad:{self.ad},Hesap no:{self.hesapno},Bakiye:{self.bakiye}"
    

class Banka:
    def __init__(self):
        self.kullanicilar = []

    def hesapac(self,ad,hesapno,bakiye):
        if not self.hesapno_varmi(hesapno):
            yeni_kullanici = Kullanici(ad,hesapno,bakiye)
            self.kullanicilar.append(yeni_kullanici)
    
    def hesapno_varmi(self,hesapno):
        for kullanici in self.kullanicilar:
            if kullanici.hesapno == hesapno:
                return True 
            return False 
                
    def kullanicibul(self,hesapno):
        for kullanici in self.kullanicilar:
            if kullanici.hesapno == hesapno:
                return kullanici
            return None
    
    def parayatir(self,hesapno,miktar):
        kullanici = self.kullanicibul(hesapno)
        if kullanici:
            return kullanici.parayatir(miktar)
        return False
    
    def paracek(self,hesapno,miktar):
        kullanici = self.kullanicibul(hesapno)
        if kullanici:
            return kullanici.paracek(miktar)
        return False
    
    def bakiyesorgula(self,hesapno):
        kullanici = self.kullanicibul(hesapno)
        if kullanici:
            return kullanici.bakiye
        return None
    
    def kullanicilistele(self):
        for kullanici in self.kullanicilar:
            print(kullanici)

if __name__ == "__main__":
    banka = Banka()

    while True:
        print("1.Hesap Aç")
        print("2.Para Yatır")
        print("3.Para Çek")
        print("4.Bakiye Sorgula")
        print("5.Kullanici Listele")
        print("6.Çikiş")

        secim = input("bir seçim yapin:")

        if secim == "1":
            ad = input("Adiniz")
            hesapno = input("hesap numaraniz")
            bakiye = float(input("baslangic bakiyesi"))
            if banka.hesapac(ad,hesapno,bakiye):
                print("hesap başariyla olusturuldu")
            
        elif secim == "2":
            hesapno = input("hesap numaraniz")
            miktar = float(input("yatirilacak miktar"))
            if banka.parayatir(hesapno,miktar):
                print("para basariyla yatirildi.")
            
        elif secim == "3":
            hesapno = input("hesap numaranız")
            miktar = float(input("cekilecek miktar"))
            if banka.paracek(hesapno,miktar):
                print("Para çekildi")
        
        elif secim =="4":
            hesapno = input("hesap numaraniz")
            bakiye = banka.bakiyesorgula(hesapno)
            if bakiye is not None:
                print(f"Bakiyeniz:{bakiye} TL")
            else:
                print("hesap bulunamadi")
        
        elif secim == "5":
            banka.kullanicilistele()
        
        elif secim == "6":
            print("Cikis yapiliyor")

