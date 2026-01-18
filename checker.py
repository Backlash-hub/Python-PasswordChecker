import string
import tkinter as tk
from tkinter import *

def get_user_input():
    root = tk.Tk()
    root.title("Password testing")
    root.geometry("300x150")
    
    password_var = tk.StringVar()
    result_var = tk.StringVar(value="")


    password_label = tk.Label(root, text="Password")
    password_entry = tk.Entry(root, textvariable=password_var, show="*")
    result_label = tk.Label(root, textvariable=result_var, font = ('calibre',10,'bold'))
    
    canvas = tk.Canvas(root, width=20, height=20, highlightthickness=0)
    circle_id = canvas.create_oval(2, 2, 18, 18, fill="gray", outline="gray") 
    
    def set_indicator(color: str):
        canvas.itemconfig(circle_id, fill=color, outline=color)


    def on_submit():
        pwd =password_var.get()
        strength = check_password_strength(pwd)
        if strength == "Strong":
            result_label.config(fg='green')
            set_indicator("green")
        elif strength == "Medium":
            result_label.config(fg='orange')
            set_indicator("orange")
        else:
            result_label.config(fg="red")
            set_indicator("red")
            
        result_var.set(f"        {strength}")

    submit_btn = tk.Button(root, text = 'Submit', command = on_submit)

    password_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    password_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    submit_btn.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    canvas.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    result_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")


    root.mainloop()


def check_password_strength(password):
    min_length= 8
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    special_characters = set(string.punctuation)
    has_special = any(c in special_characters for c in password)

    score = 0

    if len(password) >= min_length:
        score += 1
    if has_uppercase:
        score += 1
    if has_lowercase:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"
    
get_user_input()