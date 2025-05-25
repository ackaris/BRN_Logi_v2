main.py içinde yaratılan modellerin, hesaplamaının nasıl çalıştırılacağının ve HANGİ SIRAYLA YAPILMASI GEREKTİĞİNİN bir örneğini bulabilirsiniz. 

Gui4.pyw konsolsuz gui çalıştırmak içindir. Temelde yaptığı şey, mainde yapılanı kodla uğraşmadan yapmaktır. 

Programı çalıştırırken sırasıyla:

1. Konteyner özelliklerini tanımlayın (en boy genişlik)
2. Modelleri oluşturun (hangi tip, boyutlar ve kaç adet
3. Product.add ile modellerden istenen adet ürün oluşturun
4. calc ile ıra yerleştirin.

Not: Gui ile yaparken her model eklediğinizde Hesaplamayı çalıştırmanıza gerek yoktur. Önce modelleri eklemeyi bitirin daha sonra hepsi eklendiğinde hesaplamayı çalıştırın. 
Not2. Yeni hesaplama çalıştırmanız için gui'yi kapatıp tekrar çalıltırmanız gerekir henüz hafızayı temizleme fonksiyonu programa eklenmemiştir.(Talep halinde eklenecektir.)
Not3: Yerleştirme algoritmasının nasıl çalıştığıını calc.py ve layer.py içinden görebilirsiniz. Algoritma bu iki dosya üzerinden çok katmanlı mantıksal sorgulamalar ile çalışmaktadır. Veriyi Array'ler üzerinde tutar ve bunların manipülasyonu ile Containerları yerleştirir.Daha modern bir veri yapısı ile bunu yapmak elbette mümkündür ancak bu projede asıl önemli olan husus amaçlanan şeyin en hızlı bir şekilde yapılması olduğundan veri yapılarına ve bunların verimliliğine önem verilmemiştir. 
