from tkinter import *


# Converts distance in miles to distance in kms
def convert():
    dist_in_miles = int(input_text_field.get())
    dist_in_km = round(dist_in_miles * 1.609)
    result_label["text"] = dist_in_km


FONT = ("Calibri", 15)

# ----------------------------------- UI Setup ----------------------------------- #

# Window
window = Tk()
window.config(padx=20, pady=20)
window.title("Miles to Km Converter")

# Labels
is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=0, row=1)

result_label = Label(text="0", font=FONT)
result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

# Button
calc_button = Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=2)

# Entry
input_text_field = Entry(width=15)
input_text_field.grid(column=1, row=0)
input_text_field.focus()

window.mainloop()
