import tkinter as tk
from tkinter import ttk

BG = "#3b3f9e"
FG = "white"


def hasil_prediksi():
    # Apapun input yang diberikan, hasil prediksi selalu Teknologi Informasi
    label_hasil.config(text="Prediksi Prodi: Teknologi Informasi")


root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.configure(bg=BG)
root.geometry("420x640")
root.resizable(False, False)

# Judul
tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Segoe UI", 16, "bold"),
    bg=BG,
    fg=FG,
).pack(pady=(20, 15))

# Frame input 10 nilai mata pelajaran
frame_input = tk.Frame(root, bg=BG)
frame_input.pack(padx=30, pady=5)

entries = []
for i in range(10):
    tk.Label(
        frame_input,
        text=f"Nilai Mata Pelajaran {i + 1}:",
        font=("Segoe UI", 10, "bold"),
        bg=BG,
        fg=FG,
        anchor="e",
        width=22,
    ).grid(row=i, column=0, padx=(0, 10), pady=4, sticky="e")

    entry = tk.Entry(frame_input, width=18, font=("Segoe UI", 10), justify="center")
    entry.grid(row=i, column=1, pady=4)
    entries.append(entry)

# Pilihan jurusan
tk.Label(
    root,
    text="Pilihan Jurusan Anda:",
    font=("Segoe UI", 10, "bold"),
    bg=BG,
    fg=FG,
).pack(pady=(20, 4))

combo = ttk.Combobox(
    root,
    values=["Teknologi Informasi", "Sistem Informasi", "Teknik Elektro", "Manajemen"],
    state="readonly",
    width=22,
)
combo.current(0)
combo.pack()

# Tombol
tk.Button(
    root,
    text="Hasil Prediksi",
    font=("Segoe UI", 10, "bold"),
    command=hasil_prediksi,
    padx=10,
    pady=4,
).pack(pady=(20, 15))

# Label luaran
label_hasil = tk.Label(
    root,
    text="",
    font=("Segoe UI", 12, "bold"),
    bg=BG,
    fg="#7ff0ff",
)
label_hasil.pack(pady=10)

root.mainloop()