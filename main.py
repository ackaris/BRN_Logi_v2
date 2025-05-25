import container
import calc
import gui
import product
import models

#Programmed For Yigit Can Kara by ACK with <3 .
#do not touch anything but this file you will probablzy breake it if you do :)

container1= container.container(240, 1200, 269) #container boyutlarını belirle
'''Model id: Kafana göre
   r: Çapı
   h: yüksekliği(boyu)
'''
model1= models.model(1, 17, 160, 0)  #model1'i oluştur
'''
ilk attr, ürünün oluşturulacağı model
ikincisi kaç tane olacağı(tüm siparişte)
'''
product.create(model1, 460  #model1'den ürün oluştur
               )
#model2= models.model(2, 36, 200, 1, long_Edge=36)
#product.create(model2, 100 )



calc.calc() #Hesaplamayı yap her zaman ilk tanımladığın model
calc.print_stats() #statları printle
calc.showplot(container1) #yükleme şeması çiz'''
gui.illustrate_truck_volumes_gui(calc.volume_left())
print(container.container_mem)