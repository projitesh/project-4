import tkinter as tk
from tkinter import messagebox
import os

class PersonalDiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Diary")
        self.root.geometry("500x600")

        # Create widgets for new entry
        self.label_date = tk.Label(root, text="Date (YYYY-MM-DD):")
        self.label_date.pack(pady=5)

        self.entry_date = tk.Entry(root)
        self.entry_date.pack(pady=5)

        self.label_entry = tk.Label(root, text="Diary Entry:")
        self.label_entry.pack(pady=5)

        self.text_entry = tk.Text(root, wrap=tk.WORD, height=10)
        self.text_entry.pack(pady=10)

        self.button_save = tk.Button(root, text="Save Entry", command=self.save_entry)
        self.button_save.pack(pady=5)

        self.button_show = tk.Button(root, text="Show Previous Entries", command=self.show_entries)
        self.button_show.pack(pady=5)

        self.text_display = tk.Text(root, wrap=tk.WORD, height=15)
        self.text_display.pack(pady=10)

    def save_entry(self):
        date = self.entry_date.get()
        content = self.text_entry.get("1.0", tk.END)
        
        if not date or not content.strip():
            messagebox.showwarning("Warning", "Date and Entry cannot be empty!")
            return
        
        directory = "diary_entries"
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        file_path = os.path.join(directory, f"{date}.txt")
        
        with open(file_path, "w") as file:
            file.write(content)
        
        messagebox.showinfo("Success", f"Entry saved for {date}")
        self.entry_date.delete(0, tk.END)
        self.text_entry.delete("1.0", tk.END)

    def show_entries(self):
        self.text_display.delete("1.0", tk.END)
        directory = "diary_entries"
        if not os.path.exists(directory):
            messagebox.showwarning("Warning", "No entries found!")
            return
        
        files = os.listdir(directory)
        if not files:
            messagebox.showwarning("Warning", "No entries found!")
            return
        
        for file_name in files:
            file_path = os.path.join(directory, file_name)
            with open(file_path, "r") as file:
                content = file.read()
                date = file_name.replace(".txt", "")
                self.text_display.insert(tk.END, f"Date: {date}\n{content}\n{'-'*40}\n")

# Create the main window
root = tk.Tk()
app = PersonalDiaryApp(root)
root.mainloop()
