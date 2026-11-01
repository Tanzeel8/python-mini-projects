# Line-by-line PDF translation: English to Urdu (MyMemory translator)
import threading
import time
import tkinter as tk
from tkinter import filedialog, messagebox

import fitz  # PyMuPDF
from deep_translator import MyMemoryTranslator

# Optional: put your email here to raise the free daily limit
# (about 5,000 characters/day without email, about 50,000 with email).
EMAIL = ""


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


def safe_translate(translator, text, retries=3):
    """Translate one line; retry with a wait if the server complains."""
    for attempt in range(retries):
        try:
            result = translator.translate(text)
            if result and "MYMEMORY WARNING" in result.upper():
                return "[Daily free limit reached. Try again tomorrow or add EMAIL in the code.]"
            return result or text
        except Exception as e:
            if attempt == retries - 1:
                return f"[Translation failed: {e}]"
            time.sleep(2 * (attempt + 1))  # wait 2s, 4s


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
        kwargs = {"source": "english", "target": "urdu"}
        if EMAIL:
            kwargs["email"] = EMAIL
        translator = MyMemoryTranslator(**kwargs)
        found_text = False

        with fitz.open(file_path) as doc:
            for page in doc:
                for line in page.get_text("text").split("\n"):
                    line = line.strip()
                    if not line:
                        continue
                    found_text = True
                    translated = safe_translate(translator, line)
                    time.sleep(0.3)  # be gentle with the server
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
