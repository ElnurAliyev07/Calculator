import tkinter as tk
from tkinter import messagebox


def press(key):
    if key == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            entry.delete(0, tk.END)
    elif key == "C":
        entry.delete(0, tk.END)
    elif key == "←":
        current_text = entry.get()
        entry.delete(len(current_text) - 1, tk.END)
    else:
        entry.insert(tk.END, key)


def on_button(button_text):
    press(button_text)


root = tk.Tk()
root.title("Calculator")

root.resizable(False, False)

entry = tk.Entry(root, width=20, font=('Arial', 14), bd=10, relief=tk.SUNKEN, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    '1', '2', '3', '←',
    '4', '5', '6', '+',
    '7', '8', '9', '-',
    '(', '0', ')', '*',
    'C', '.', '=', '/'
]

row = 1
col = 0
for button in buttons:
    tk.Button(root, text=button, width=4, height=1, font=('Arial', 14), bd=8, command=lambda bt=button: on_button(bt)) \
        .grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
