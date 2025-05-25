import tkinter as tk
from tkinter import messagebox
import container
import calc
import product
import models
from tkinter import ttk
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

def illustrate_truck_volumes_gui(volumes):
    root = tk.Tk()
    root.title("🚛 Tır Doluluk Rehberi")
    root.geometry("700x500")  # Pencere boyutu

    # Başlık
    title = tk.Label(root, text="🚛 Tır Doluluk Rehberi", font=("Helvetica", 20, "bold"))
    title.pack(pady=20)

    # Her tır için bir satır oluştur
    for i, percent in enumerate(volumes):
        frame = tk.Frame(root)
        frame.pack(fill='x', padx=30, pady=10)

        label = tk.Label(
            frame,
            text=f"🚛  Tır {i+1} — % {percent:.1f}",
            font=("Helvetica", 16),
            width=25,
            anchor='w'
        )
        label.pack(side='left')

        progress = ttk.Progressbar(frame, length=300, mode='determinate')
        progress['value'] = percent
        progress.pack(side='left', padx=20, ipady=6)  # Bar kalınlığı gibi

    root.mainloop()
