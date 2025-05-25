import container
import calc
import product
import models

#Programmed For Yigit Can Kara by ACK with <3 .
#do not touch anything but this file you will probablzy breake it if you do :)

'''container1=container.container(234,1200,269) #container boyutlarını belirle'''
'''Model id: Kafana göre
   r: Çapı
   h: yüksekliği(boyu)
'''
'''model1=models.model(1,17,160)  #model1'i oluştur'''
'''
ilk attr, ürünün oluşturulacağı model
ikincisi kaç tane olacağı(tüm siparişte)
'''
'''product.create(model1,200 #model1'den ürün oluştur
               )
model2=models.model(2,10,150)
product.create(model2,1000
               )


calc.calc(container1,model1) #Hesaplamayı yap her zaman ilk tanımladığın model
calc.print_stats() #statları printle
calc.showplot(container1) #yükleme şeması çiz'''
import tkinter as tk
from tkinter import messagebox


models_list = []

def run_gui():
    root = tk.Tk()
    root.title("Konteyner Yükleme Hesaplayıcı")

    tk.Label(root, text="Konteyner Genişliği").pack()
    cont_width_entry = tk.Entry(root)
    cont_width_entry.pack()

    tk.Label(root, text="Konteyner Yüksekliği").pack()
    cont_height_entry = tk.Entry(root)
    cont_height_entry.pack()

    tk.Label(root, text="Konteyner Uzunluğu").pack()
    cont_length_entry = tk.Entry(root)
    cont_length_entry.pack()

    # Model input
    tk.Label(root, text="Model ID").pack()
    model_id_entry = tk.Entry(root)
    model_id_entry.pack()

    tk.Label(root, text="Model Yarıçapı (r)").pack()
    model_r_entry = tk.Entry(root)
    model_r_entry.pack()

    tk.Label(root, text="Model Yüksekliği (h)").pack()
    model_h_entry = tk.Entry(root)
    model_h_entry.pack()

    tk.Label(root, text="Adet").pack()
    model_count_entry = tk.Entry(root)
    model_count_entry.pack()

    def add_model():
        try:
            m_id = int(model_id_entry.get())
            r = float(model_r_entry.get())
            h = float(model_h_entry.get())
            count = int(model_count_entry.get())

            m = models.model(m_id, r, h)
            product.create(m, count)
            models_list.append(m)
            messagebox.showinfo("Başarılı", f"Model {m_id} eklendi.")
        except Exception as e:
            messagebox.showerror("Hata", str(e))

    def run_calculation():
        try:
            w = float(cont_width_entry.get())
            l = float(cont_height_entry.get())
            h = float(cont_length_entry.get())

            container1 = container.container(w, h, l)
            if not models_list:
                messagebox.showwarning("Uyarı", "En az bir model eklemelisiniz.")
                return

            # Sadece ilk modeli kullandığını varsayıyoruz, istersen çoklu destekleyebiliriz.
            calc.calc(container1, models_list[0])
            calc.print_stats()
            calc.showplot(container1)
        except Exception as e:
            messagebox.showerror("Hata", str(e))

    tk.Button(root, text="Model Ekle", command=add_model).pack(pady=5)
    tk.Button(root, text="Hesaplamayı Çalıştır", command=run_calculation).pack(pady=10)

    root.mainloop()
run_gui()