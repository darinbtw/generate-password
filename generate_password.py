import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор паролей")
        self.root.geometry("400x300")

        # Запрет изменения размеров окна
        self.root.resizable(width=False, height=False)

        self.password_var = tk.StringVar()

        self.create_widgets()

    def generate_password(self):
        length = 15  # Длина пароля (можете изменить по своему усмотрению)
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for i in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        self.root.update()
        messagebox.showinfo("Скопировано", "Пароль скопирован в буфер обмена.")

    def create_widgets(self):
        # Этикетка для отображения пароля
        password_label = tk.Label(self.root, text="Пароль:")
        password_label.pack(pady=10)

        # Поле для отображения пароля
        password_entry = tk.Entry(self.root, textvariable=self.password_var, state='readonly', width=20)
        password_entry.pack(pady=10)

        # Кнопка "Создать новый пароль"
        generate_button = tk.Button(self.root, text="Создать новый пароль", command=self.generate_password)
        generate_button.pack(pady=10)

        # Кнопка "Скопировать в буфер обмена"
        copy_button = tk.Button(self.root, text="Скопировать в буфер обмена", command=self.copy_to_clipboard)
        copy_button.pack(pady=10)

        # Кнопка "Выход"
        exit_button = tk.Button(self.root, text="Выход", command=self.root.destroy)
        exit_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
