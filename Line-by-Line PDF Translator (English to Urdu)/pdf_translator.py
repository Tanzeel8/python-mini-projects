# Line-by-line PDF translation: English to Urdu
import threading
import tkinter as tk
from tkinter import filedialog, messagebox

import fitz  # PyMuPDF
from deep_translator import GoogleTranslator


def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        entry_pdf_path.delete(0, tk.END)
        entry_pdf_path.insert(0, file_path)


def append_text(text):
    output_text.insert(tk.END, text)
    output_text.see(tk.END)


def finish(error=None):
    btn_translate.config(state=tk.NORMAL)
    if error:
        messagebox.showerror("Error", error)


def translate_pdf():
    file_path = entry_pdf_path.get().strip()
    if not file_path.lower().endswith(".pdf"):
        messagebox.showerror("Error", "Please select a valid PDF file.")
        return

    output_text.delete("1.0", tk.END)
    btn_translate.config(state=tk.DISABLED)
    threading.Thread(target=translate_pdf_thread, args=(file_path,), daemon=True).start()


def translate_pdf_thread(file_path):
    try:
        translator = GoogleTranslator(source="en", target="ur")
        found_text = False

        with fitz.open(file_path) as doc:
            for page in doc:
                for line in page.get_text("text").split("\n"):
                    line = line.strip()
                    if not line:
                        continue
                    found_text = True
                    try:
                        translated = translator.translate(line) or line
                    except Exception as e:
                        translated = f"[Translation failed: {e}]"
                    root.after(0, append_text, f"English: {line}\nUrdu: {translated}\n\n")

        if found_text:
            root.after(0, finish)
        else:
            root.after(0, finish, "No text found. This PDF may be scanned (images only).")
    except Exception as e:
        root.after(0, finish, str(e))


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
