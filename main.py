import tkinter as tk
from tkinter import messagebox as msg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# Initialize root window
root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("800x600")
root.iconbitmap(r"main-logo.ico")
root.configure(background="#f7ffff")

file = None  # Track opened file

# Create Text Area
text_area = tk.Text(root, font="Arial 13", wrap="word", undo=True)
text_area.pack(fill="both", expand=True)

# Create Scrollbar
scrollbar = tk.Scrollbar(text_area, command=text_area.yview)
scrollbar.pack(side="right", fill="y")
text_area.config(yscrollcommand=scrollbar.set)

# Create Status Bar
status_bar = tk.Label(root, text="Ready", anchor="w", relief="sunken")
status_bar.pack(side="bottom", fill="x")

def update_status(message):
    status_bar.config(text=message)

def new_file():
    global file
    file = None
    root.title("Untitled - Notepad")
    text_area.delete(1.0, tk.END)
    update_status("New file created")

def open_file():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        root.title(os.path.basename(file) + " - Notepad")
        with open(file, "r", encoding="utf-8") as f:
            text_area.delete(1.0, tk.END)
            text_area.insert(1.0, f.read())
        update_status(f"Opened {file}")

def save_file():
    global file
    if file is None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                  filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if not file:
            return
    with open(file, "w", encoding="utf-8") as f:
        f.write(text_area.get(1.0, tk.END))
    root.title(os.path.basename(file) + " - Notepad")
    update_status(f"Saved {file}")

def cut_func():
    text_area.event_generate("<<Cut>>")
    update_status("Cut action performed")

def copy_func():
    text_area.event_generate("<<Copy>>")
    update_status("Copy action performed")

def paste_func():
    text_area.event_generate("<<Paste>>")
    update_status("Paste action performed")

def about():
    msg.showinfo("Notepad", "Notepad by Rakesh Sahani")

# Create Menu Bar
topmenu = tk.Menu(root)

# File Menu
file_menu = tk.Menu(topmenu, tearoff=0)
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
topmenu.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = tk.Menu(topmenu, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_func, accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", command=copy_func, accelerator="Ctrl+C")
edit_menu.add_command(label="Paste", command=paste_func, accelerator="Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=text_area.edit_undo, accelerator="Ctrl+Z")
edit_menu.add_command(label="Redo", command=text_area.edit_redo, accelerator="Ctrl+Y")
topmenu.add_cascade(label="Edit", menu=edit_menu)

# Help Menu
help_menu = tk.Menu(topmenu, tearoff=0)
help_menu.add_command(label="About", command=about)
topmenu.add_cascade(label="Help", menu=help_menu)

root.config(menu=topmenu)

# Key Bindings
root.bind("<Control-n>", lambda event: new_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<Control-x>", lambda event: cut_func())
root.bind("<Control-c>", lambda event: copy_func())
root.bind("<Control-v>", lambda event: paste_func())

root.mainloop()
