#Yapılacaklar Listesi

#Görev Sınıfı:
#görevin adı (ad) , görevin durumunu (tamamlandi) kontrol eder

#Görevleri Yönetme:
#görev ekleme (gorevekle), görev silme (gorevsil), görev tamamlama(gorevtamamla) , 
#görev listeleme (gorevlerlistele), görevleri dosyaya yükleme (gorevleriyukle) işlevlerini gerçekleştirir.

class gorev:
    
    def _init_ (self,ad):
        
        self.ad=ad 
        self.tamamlandi=False

    def tamamla(self):
        self.tamamlandi=True
        
    def _str_(self):
        durum="Tamamlandi" if self.tamamlandi else "Tamamlandi"
        return f"{self.ad}-{durum}"

class gorevyonet:
    def _init_(self,dosyaadi="gorevler.txt"):
        self.gorevler = []
        self.dosyaadi=dosyaadi
        self.gorevleriyukle()

    def gorevekle(self,gorevadi):
        gorev=Gorev(gorevadi)
        self.gorevler.append(gorev)
    
    def gorevtamamla(self,indeks):
        if 0 <=indeks<len(self.gorevler):
            self.gorevler[indeks].tamamla()
    
    def gorevsil(self,indeks):
        if 0 <=indeks<len(self.gorevler):
            delete.self.gorevler[indeks]
    
    def gorevlerlistele(self):
        print("Tamamlanmayan Görevler")
        for i , gorev in enumerate(self.gorevler):
            if not gorev.tamamlandi:
                print(f"{i}:{gorev}")
        print("Tamamlanan Görevler")
        for i , gorev in enumerate(self.gorevler):
            if gorev.tamamlandi:
                print(f"{i}:{gorev}")
    
    def gorevlerikaydet(self):
        with open(self.dosyaadi) as dosya:
            for gorev in self.gorevler:
                dosya.write(f"{gorev.ad}|{gorev.tamamlandi}")
    
    def gorevleriyukle(self):
        try:
            with open(self.dosyaadi,) as dosya:
                for satir in dosya:
                    ad,tamamlandi=satir.strip().split()
                    gorev=Gorev(ad)
                    gorev.tamamlandi=tamamlandi=="True"
                    self.gorevler.append(gorev)
        except FileNotFoundError:
            pass

if __name__=="__main__":
    yonetici=gorevyonet()

    while True:
        print("1.Görev ekle")
        print("2.Görebvleri Görüntüle")
        print("3.Görev tamamla")
        print("4.Görevleri Sil")
        print("5.Çikiş ve kaydet")
        
        secim=input("Bir seçim yap:")
    
if secim=="1":
        gorevadi = input("gorev adi:")
        yonetici.gorev_ekle(gorev_adi)
elif secim == "2":
        yonetici.gorevlerlistele()
elif secim == "3":
        indeks = int(input("tamamlanacak görev numarasi:"))
        yonetici.gorevtamamla(indeks)
elif secim == "4":
        indeks = int(input("silinecek gorevin numarasi:"))
        yonetici.gorev_sil(indeks)
elif secim == "5":
        yonetici.gorevler_kaydet()
        print("gorevler kaydedildi.")
