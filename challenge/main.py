import tkinter as tk
import math

window = tk.Tk()
window.title(string="Mile To Km Converter")
# window.minsize(width=300, height=200)
window.config(padx=40, pady=40, bg="white")

entry = tk.Entry(width=10)
entry.insert(1, "0")
entry.grid(column=1, row=0)

unit_mile = tk.Label(text="Miles", font=("Arial", 16))
unit_mile.grid(column=2, row=0)
unit_mile.config(padx=6, bg="white")

unit_is_equal = tk.Label(text="is equal to", font=("Arial", 16))
unit_is_equal.grid(column=0, row=1)
unit_is_equal.config(padx=6, bg="white")

value_km = tk.Label(text="0", font=("Arial", 16))
value_km.grid(column=1, row=1)
value_km.config(padx=6, bg="white")

unit_km = tk.Label(text="Km", font=("Arial", 16))
unit_km.grid(column=2, row=1)
unit_km.config(padx=6, bg="white")


def covert_to_km():
    km = int(entry.get()) * 1.609  # int can be used to generate float type
    value_km.config(text=(math.ceil(km * 100)) / 100)


button_cal = tk.Button(text="Calculator", bg="white", command=covert_to_km)
button_cal.grid(column=1, row=2)

window.mainloop()
