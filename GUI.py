import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("This is a GUI")
root.geometry("700x500")

def load_csv():
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    print(f"Loaded file: {filename}")

load_button = tk.Button(root, text="upload CSV", command=load_csv)
load_button.pack(pady=200)
root.mainloop()
