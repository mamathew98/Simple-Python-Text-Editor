import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from custome_notebook import CustomNotebook

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")
        self.master.geometry("800x600")

        self.notebook = CustomNotebook(width=200, height=200)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.new_tab()

        # Theme variable
        self.theme = "light"

        self.menubar = tk.Menu(self.master)
        self.master.config(menu=self.menubar)

        file_menu = tk.Menu(self.menubar, tearoff=False)
        file_menu.add_command(label="New Tab", command=self.new_tab)
        self.menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit_app)

        preferences_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Preferences", menu=preferences_menu)
        preferences_menu.add_command(label="Dark Theme", command=lambda: self.set_theme("dark"))
        preferences_menu.add_command(label="Light Theme", command=lambda: self.set_theme("light"))

        help_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Help", command=self.show_help)
        
    
    def quit_app(self):
        answer = tk.messagebox .askyesno(title='Exit Editor',
                    message='Are you sure that you want to quit?')
        if answer:
            self.master.destroy()

    def open_file(self):
        options = {}
        options["defaultextension"] = ".txt"
        options["filetypes"] = [("Text Files", "*.txt"), ("All Files", "*.*")]
        options["initialdir"] = "C:\\"
        options["title"] = "Open File"
        file_path = filedialog.askopenfilename(**options)
        if not file_path:
            return
        with open(file_path, "r") as file:
            text = file.read()

        self.new_tab()

        tab = self.get_current_tab()            
        tab.delete("1.0", tk.END)
        tab.insert(tk.END, text)
        self.master.title(f"Text Editor - {file_path}")
        self.notebook.tab(tab, text=file_path)

    def save_file(self):
        options = {}
        options["defaultextension"] = ".txt"
        options["filetypes"] = [("Text Files", "*.txt"), ("All Files", "*.*")]
        options["initialdir"] = "C:\\"
        options["title"] = "Save File"
        file_path = filedialog.asksaveasfilename(**options)
        if not file_path:
            return
        with open(file_path, "w") as file:
            text = self.get_current_tab().get("1.0", tk.END)
            file.write(text)
        self.notebook.tab(self.get_current_tab(), text=file_path)

    def new_tab(self):
        tab = tk.Text(self.notebook)
        self.notebook.add(tab, text="Untitled")
        self.notebook.select(tab)

    def set_theme(self, theme):
        tabs = self.notebook.winfo_children()
        if theme == "light":
            self.theme = "light"
            self.master.configure(bg="#FFFFFF")
            for tab in tabs:
                tab.configure(bg="#FFFFFF", fg="#000000")
        else:
            self.theme = "dark"
            self.master.configure(bg="#1C1C1E")
            for tab in tabs:
                tab.configure(bg="#1C1C1E", fg="#FFFFFF")

    def show_help(self):
        messagebox.showinfo("Help", "This is a simple text editor created using Python Tkinter. "
                            "You can create multiple tabs and edit text in each tab.")

    def get_current_tab(self):
        return self.notebook.winfo_children()[self.notebook.index(self.notebook.select())]

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()

