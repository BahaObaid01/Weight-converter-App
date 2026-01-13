import customtkinter as ctk
import tkinter.messagebox as messagebox

def convert_weight():
    try:
        weight = float(entry_weight.get())
        unit = entry_unit.get().strip().lower()

        if unit == "l":
            result = weight * 2.205
            result_unit = "Lbs"
        elif unit == "k":
            result = weight / 2.205
            result_unit = "Kgs"
        else:
            messagebox.showerror("Error", "Unit must be K or L")
            return

        label_result.configure(text=f"Your weight is: {round(result, 1)} {result_unit}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

#UI
ctk.set_appearance_mode("dark")     
ctk.set_default_color_theme("blue") 

app = ctk.CTk()
app.title("Weight Converter")
app.geometry("360x260")
app.resizable(False, False)

title = ctk.CTkLabel(app, text="Weight Converter", font=("Arial", 20, "bold"))
title.pack(pady=(20, 10))

entry_weight = ctk.CTkEntry(app, placeholder_text="Enter weight (e.g., 70)")
entry_weight.pack(pady=8, padx=30, fill="x")

entry_unit = ctk.CTkEntry(app, placeholder_text="Unit: K or L")
entry_unit.pack(pady=8, padx=30, fill="x")

btn = ctk.CTkButton(app, text="Convert", command=convert_weight)
btn.pack(pady=15, padx=30, fill="x")

label_result = ctk.CTkLabel(app, text="", font=("Arial", 14))
label_result.pack(pady=10)

app.mainloop()
