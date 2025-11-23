from PIL import Image
from tkinter import filedialog
import tkinter as tk
import re

def numeric_sort(file_list):
    return sorted(file_list, key=lambda x: int(re.findall(r'\d+', x)[-1]))

# Root oluştur ama tamamen gizle
root = tk.Tk()
root.overrideredirect(True)
root.withdraw()

# PNG seçme
file_paths = filedialog.askopenfilenames(
    title="PDF'e dönüştürülecek PNG dosyalarını seç",
    filetypes=[("PNG Files", "*.png")],
    parent=root
)

if not file_paths:
    print("Dosya seçilmedi.")
    root.destroy()
    exit()

file_paths = numeric_sort(file_paths)

images = [Image.open(fp).convert("RGB") for fp in file_paths]

first = images[0]
rest = images[1:]

# PDF kaydetme yeri seçme
save_path = filedialog.asksaveasfilename(
    title="PDF olarak kaydet",
    defaultextension=".pdf",
    filetypes=[("PDF Files", "*.pdf")],
    parent=root
)

root.destroy()

if save_path:
    first.save(save_path, save_all=True, append_images=rest)
    print("PDF başarıyla oluşturuldu:", save_path)
else:
    print("Kaydetme iptal edildi.")
