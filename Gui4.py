import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import json
import container
import calc
import product
import models
import gui

# Tkinter ana pencere
root = tk.Tk()
root.title("Yükleme Hesaplayıcı GUI")
root.geometry("900x500")

# Model tipleri için dropdown değerleri
model_types = ["Rollpack", "Box", "Flatpack"]

# Sol panel - Model ekleme formu
form_frame = tk.Frame(root, padx=10, pady=10)
form_frame.pack(side=tk.LEFT, fill=tk.Y)

# Default container checkboxu
use_default_container = tk.BooleanVar(value=True)
def on_default_toggle():
    if use_default_container.get():
        contw_entry.configure(state='disabled')
        conth_entry.configure(state='disabled')
        contl_entry.configure(state='disabled')
    else:
        contw_entry.configure(state='normal')
        conth_entry.configure(state='normal')
        contl_entry.configure(state='normal')

chk_default = tk.Checkbutton(form_frame, text="Varsayılan Container (240x1200x269)", variable=use_default_container, command=on_default_toggle)
chk_default.pack()

# Container ölçüleri
tk.Label(form_frame, text="Cont Genişlik").pack()
contw_entry = tk.Entry(form_frame)
contw_entry.pack()

tk.Label(form_frame, text="Cont Yükseklik").pack()
conth_entry = tk.Entry(form_frame)
conth_entry.pack()

tk.Label(form_frame, text="Cont Uzunluk").pack()
contl_entry = tk.Entry(form_frame)
contl_entry.pack()

on_default_toggle()  # Başlangıçta default ayarları uygula

# Container tanımı fonksiyonu (hesaplamadan önce çağrılacak)
def define_container():
    if use_default_container.get():
        return container.container(240, 1200, 269)
    else:
        w = float(contw_entry.get())
        l = float(contl_entry.get())
        h = float(conth_entry.get())
        return container.container(w, l, h)

# Model giriş alanları
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

# Eklenen modeller listesi
added_models = []

def add_model():
    try:
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

        added_models.append((model, count))
        product.create(model, count)

        model_listbox.insert(tk.END, f"Model ID {model.id}: {count} adet ({model_type})")

        entry_r.delete(0, tk.END)
        entry_h.delete(0, tk.END)
        entry_count.delete(0, tk.END)
        entry_long_edge.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Hata", f"Model eklenemedi: {e}")

def save_models():
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if not file_path:
            return
        data = [
            {
                'id': model.id,
                'r': model.r,
                'h': model.h,
                'model_id': model.model_id,
                'long_Edge': getattr(model, 'long_Edge', None),
                'count': count
            } for model, count in added_models
        ]
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        messagebox.showinfo("Başarılı", "Model listesi kaydedildi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Kaydedilemedi: {e}")

def load_models():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if not file_path:
            return
        with open(file_path, 'r') as f:
            data = json.load(f)
        added_models.clear()
        model_listbox.delete(0, tk.END)
        for item in data:
            model = models.model(item['id'], item['r'], item['h'], item['model_id'], long_Edge=item.get('long_Edge'))
            added_models.append((model, item['count']))
            product.create(model, item['count'])
            model_type = "Rollpack" if item['model_id'] == 0 else "Box/Flatpack"
            model_listbox.insert(tk.END, f"Model ID {model.id}: {item['count']} adet ({model_type})")
        messagebox.showinfo("Başarılı", "Model listesi yüklendi.")
        run_calculation()
    except Exception as e:
        messagebox.showerror("Hata", f"Yüklenemedi: {e}")

def background_calc():
    try:
        global container1
        container1 = define_container()
        calc.calc()
        calc.print_stats()
        root.after(0, show_results)
    except Exception as e:
        root.after(0, lambda: messagebox.showerror("Hesaplama Hatası", str(e)))

def show_results():
    try:
        calc.showplot(container1)
        gui.illustrate_truck_volumes_gui(calc.volume_left())
        messagebox.showinfo("Kalan Hacim", f"Kalan Hacim: {calc.volume_left()} cm3")
    except Exception as e:
        messagebox.showerror("Görselleştirme Hatası", str(e))

def run_calculation():
    threading.Thread(target=background_calc).start()

# Butonlar için ayrı bir çerçeve
button_frame = tk.Frame(form_frame, pady=10)
button_frame.pack()

btn_add = tk.Button(button_frame, text="Model Ekle", command=add_model)
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_save = tk.Button(button_frame, text="Kaydet", command=save_models)
btn_save.grid(row=0, column=1, padx=5, pady=5)

btn_load = tk.Button(button_frame, text="Yükle", command=load_models)
btn_load.grid(row=0, column=2, padx=5, pady=5)

btn_calc = tk.Button(button_frame, text="Hesaplamayı Çalıştır", command=run_calculation, bg="lightgreen")
btn_calc.grid(row=1, column=0, columnspan=3, pady=15, ipadx=10)

# Sağ panel - Eklenen modellerin listesi
list_frame = tk.Frame(root, padx=10, pady=10)
list_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

model_listbox = tk.Listbox(list_frame)
model_listbox.pack(fill=tk.BOTH, expand=True)

root.mainloop()
