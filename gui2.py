import tkinter as tk
from tkinter import ttk, messagebox
import container
import calc
import product
import models
import gui

# Sabit container tanimi
container1 = container.container(240, 1200, 269)

# Model listesi (ekranda görüntülenecek)
added_models = []

# Tkinter ana pencere
root = tk.Tk()
root.title("Yükleme Hesaplayıcı GUI")
root.geometry("900x500")

# Model tipleri için dropdown değerleri
model_types = ["Rollpack", "Box", "Flatpack"]

# Sol panel - Model ekleme formu
form_frame = tk.Frame(root, padx=10, pady=10)
form_frame.pack(side=tk.LEFT, fill=tk.Y)

tk.Label(form_frame, text="Model Çapı (r)").pack()
entry_r = tk.Entry(form_frame)
entry_r.pack()

tk.Label(form_frame, text="Model Yüksekliği (h)").pack()
entry_h = tk.Entry(form_frame)
entry_h.pack()

tk.Label(form_frame, text="Model Adedi").pack()
entry_count = tk.Entry(form_frame)
entry_count.pack()

tk.Label(form_frame, text="Model Tipi").pack()
model_type_var = tk.StringVar()
model_type_dropdown = ttk.Combobox(form_frame, textvariable=model_type_var, values=model_types)
model_type_dropdown.current(0)
model_type_dropdown.pack()

tk.Label(form_frame, text="Long Edge").pack()
entry_long_edge = tk.Entry(form_frame)
entry_long_edge.pack()
entry_long_edge.configure(state='disabled')

def on_model_type_change(event):
    selected = model_type_var.get()
    if selected == "Rollpack":
        entry_long_edge.configure(state='disabled')
        entry_long_edge.delete(0, tk.END)
    else:
        entry_long_edge.configure(state='normal')

model_type_dropdown.bind("<<ComboboxSelected>>", on_model_type_change)

def add_model():

        r = float(entry_r.get())
        h = float(entry_h.get())
        count = int(entry_count.get())
        model_type = model_type_var.get()

        if model_type == "Rollpack":
            model_id = 0
            model = models.model(len(added_models) + 1, r, h, model_id)
        else:
            model_id = 1
            long_edge = float(entry_long_edge.get()) if entry_long_edge.get() else r
            model = models.model(len(added_models) + 1, r, h, model_id, long_Edge=long_edge)

        added_models.append(model)
        product.create(model, count)

        model_listbox.insert(tk.END, f"Model ID {model.id} : {count} adet ({model_type})")

        entry_r.delete(0, tk.END)
        entry_h.delete(0, tk.END)
        entry_count.delete(0, tk.END)
        entry_long_edge.delete(0, tk.END)

btn_add = tk.Button(form_frame, text="Model Ekle", command=add_model)
btn_add.pack(pady=10)

def run_calculation():
    try:
        calc.calc()
        calc.print_stats()

        calc.showplot(container1)
        gui.illustrate_truck_volumes_gui(calc.volume_left())
        messagebox.showinfo("Kalan Hacim", f"Kalan Hacim: {calc.volume_left()} cm3")
    except Exception as e:
        messagebox.showerror("Hesaplama Hatası", str(e))

btn_calc = tk.Button(form_frame, text="Hesaplamayı Çalıştır", command=run_calculation)
btn_calc.pack(pady=20)

# Sağ panel - Eklenen modellerin listesi
list_frame = tk.Frame(root, padx=10, pady=10)
list_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

model_listbox = tk.Listbox(list_frame)
model_listbox.pack(fill=tk.BOTH, expand=True)

root.mainloop()