#gui.py

import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk
from ttkbootstrap import Style
from organizer import organize_folder
import os

class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("800x650")

        # Set minimum size for the window (prevents it from becoming too small)
        self.root.minsize(800, 650)

        # Set up Material Design style with ttkbootstrap
        self.style = Style(theme="darkly")
        
        # Apply rounded corners and other customizations
        self.style.configure("TButton", font=("Courier", 12, "bold"), padding=6)
        self.style.configure("TEntry", font=("Courier", 12), padding=6)

        # Main Frame
        self.frame = ttk.Frame(root, padding=20, relief="flat")
        self.frame.pack(fill="both", expand=True)

        # Title
        self.title_label = ttk.Label(self.frame, text="Organize Your Files!", font=("Courier", 18, "bold"), bootstyle="info")
        self.title_label.place(relx=0.5, y=30, anchor="n")

        # Folder path entry field
        self.folder_entry_label = ttk.Label(self.frame, text="Enter or browse folder path:", font=("Courier", 12))
        self.folder_entry_label.place(relx=0.5, y=100, anchor="n")

        # Entry widget for manual path input
        self.folder_path_entry = ttk.Entry(self.frame, font=('Courier', 11), bootstyle="primary", justify="left")
        self.folder_path_entry.place(relx=0.5, y=130, anchor="n", width=self.calculate_entry_width())

        # Browse Button
        self.browse_button = ttk.Button(self.frame, text="Browse", width=10, bootstyle="info", command=self.select_folder)
        self.browse_button.place(relx=0.5, y=175, anchor="n") 

        # Exception Path entry
        self.exception_label = ttk.Label(self.frame, text="Enter file/folder to ignore:\n already ignore folder 'DoNotTouch'", font=("Courier", 12), anchor="center", justify="center")
        self.exception_label.place(relx=0.5, y=240, anchor="n")

        # Entry widget for exception input
        self.exception_entry = ttk.Entry(self.frame, font=('Courier', 11), bootstyle="primary", justify="left")
        self.exception_entry.place(relx=0.5, y=290, anchor="n", width=self.calculate_entry_width())

        # Add Exception Button
        self.add_exception_button = ttk.Button(
            self.frame, text="Add Exception", width=20, bootstyle="info", command=self.add_exception)
        self.add_exception_button.place(relx=0.5, y=335, anchor="n")

        # Listbox to display exceptions
        self.exception_listbox_label = ttk.Label(self.frame, text="Exceptions List:", font=("Courier", 12))
        self.exception_listbox_label.place(relx=0.5, y=380, anchor="n")

        self.exception_listbox = tk.Listbox(self.frame, width=40, height=5, font=('Courier', 11), selectmode=tk.SINGLE, bd=2, relief="flat", bg="#2E2E2E", fg="white")
        self.exception_listbox.place(relx=0.5, y=380, anchor="n", width=self.calculate_entry_width())

        # Bind the Delete key to remove selected exception
        self.exception_listbox.bind("<Delete>", self.delete_exception)

        # Start Organizing Button with hover effect
        self.organize_button = ttk.Button(
            self.frame, text="Start Organizing", width=20, bootstyle="info", state=tk.DISABLED, command=self.start_organizing)
        self.organize_button.place(relx=0.5, y=510, anchor="n")

        # Status display with a progress bar
        self.progress = ttk.Progressbar(self.frame, length=300, mode="determinate", bootstyle="primary", maximum=100)
        self.progress.place(relx=0.5, y=560, anchor="n")

        self.status_label = ttk.Label(self.frame, text="", font=('Courier', 12))
        self.status_label.place(relx=0.5, y=580, anchor="n")

        # Initialize exception list
        self.exception_list = []

        # Bind the Entry widget to check for folder path validity
        self.folder_path_entry.bind("<KeyRelease>", self.check_path_validity)

        # Bind the window resize event to dynamically adjust the width
        self.root.bind("<Configure>", self.adjust_width)

    def delete_exception(self, event):
        # Get the index of the selected item
        selected_index = self.exception_listbox.curselection()
        
        if selected_index:
            # Get the value of the selected item
            exception_to_delete = self.exception_listbox.get(selected_index)

            # Remove the exception from the list and the listbox
            self.exception_list.remove(exception_to_delete)
            self.exception_listbox.delete(selected_index)
        else:
            messagebox.showwarning("No Selection", "Please select an exception to delete.")

    def adjust_width(self, event):
        min_width = 400
        max_width = 800
        entry_width = self.root.winfo_width() * 0.8
        entry_width = max(min_width, min(entry_width, max_width))
        
        self.folder_path_entry.place_configure(width=entry_width)
        self.exception_entry.place_configure(width=entry_width)
        self.exception_listbox.place_configure(width=entry_width)

    def calculate_entry_width(self):
        min_width = 400
        max_width = 800
        entry_width = self.root.winfo_width() * 0.8
        entry_width = max(min_width, min(entry_width, max_width))
        
        return entry_width

    def select_folder(self):
        folder_path = filedialog.askdirectory(title="Select Folder")
        if folder_path:
            self.folder_path_entry.delete(0, tk.END)
            self.folder_path_entry.insert(0, folder_path)
            self.check_path_validity(None)

    def check_path_validity(self, event):
        folder_path = self.folder_path_entry.get().strip()

        if folder_path and os.path.isdir(folder_path):
            self.organize_button.config(state=tk.NORMAL)
        else:
            self.organize_button.config(state=tk.DISABLED)

    def add_exception(self):
        exception_path = self.exception_entry.get().strip()

        if exception_path and exception_path not in self.exception_list:
            self.exception_list.append(exception_path)
            self.exception_listbox.insert(tk.END, exception_path)
            self.exception_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Invalid Entry", "Please enter a valid and unique exception path.")

    def start_organizing(self):
        folder_path = self.folder_path_entry.get().strip()
        ignore_paths = self.exception_list

        if not folder_path:
            messagebox.showwarning("Warning", "Please enter or select a valid folder path.")
            return

        self.status_label.config(text="Organizing...")
        self.progress.start()
        self.root.update_idletasks()

        result = organize_folder(folder_path, ignore_paths)

        self.progress.stop()
        self.status_label.config(text=result)
        if "❌" in result:
            messagebox.showerror("Error", result)
        else:
            messagebox.showinfo("Success", result)

if __name__ == "__main__":
    root = ttk.Window(themename="darkly")  # Dark theme for modern look
    app = FileOrganizerApp(root)
    root.mainloop()
