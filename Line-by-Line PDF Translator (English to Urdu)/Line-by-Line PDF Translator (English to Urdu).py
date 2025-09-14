#line by line translation into Urdu 

import tkinter as tk
from tkinter import filedialog, messagebox
import fitz  # PyMuPDF
from deep_translator import GoogleTranslator
import threading

def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        entry_pdf_path.delete(0, tk.END)
        entry_pdf_path.insert(0, file_path)

def translate_pdf():
    output_text.delete("1.0", tk.END)
    file_path = entry_pdf_path.get()

    if not file_path.endswith(".pdf"):
        messagebox.showerror("Error", "Please select a valid PDF file.")
        return

    # Separate thread to avoid GUI freezing
    threading.Thread(target=translate_pdf_thread, args=(file_path,)).start()

def translate_pdf_thread(file_path):
    try:
        doc = fitz.open(file_path)
        for page in doc:
            lines = page.get_text("text").split("\n")
            for line in lines:
                if line.strip():
                    translated = GoogleTranslator(source='auto', target='ur').translate(line)
                    output = f"English: {line}\nUrdu: {translated}\n\n"
                    output_text.insert(tk.END, output)
        doc.close()
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("PDF Translator - English to Urdu")
root.geometry("800x600")

frame = tk.Frame(root)
frame.pack(pady=10)

entry_pdf_path = tk.Entry(frame, width=60)
entry_pdf_path.pack(side=tk.LEFT, padx=5)

btn_browse = tk.Button(frame, text="Browse PDF", command=select_pdf)
btn_browse.pack(side=tk.LEFT, padx=5)

btn_translate = tk.Button(root, text="Translate PDF", command=translate_pdf)
btn_translate.pack(pady=5)

output_text = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
