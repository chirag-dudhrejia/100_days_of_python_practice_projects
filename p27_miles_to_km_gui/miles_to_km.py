import tkinter
from tkinter import *

window = Tk()
window.title("Miles-to-Km Converter")
window.minsize(width=600, height=350)
window.resizable(False, False)
window.config(pady=50, padx=80)


def convert():
    miles = int(mile_entry.get())
    km = miles * 1.609344
    km_display.config(text=f"{km:.2f}")


headline = Label(text="!! Enter Miles to convert into Kilometers !!", font=("", 16), height=2)
headline.grid(column=0, row=0)

mile_entry = Entry(width=30)
mile_entry.insert(END, string="0")
mile_entry.grid(column=0, row=1, sticky=tkinter.N + tkinter.E + tkinter.W + tkinter.S)

mile_label = Label(text=" Miles", font=("", 14), anchor="w")
mile_label.grid(column=6, row=1)

equal_label = Label(text="||", font=("", 14))
equal_label.grid(column=0, row=2)

km_display = Label(text="0", width=30, anchor="w", padx=4, relief="sunken")
km_display.grid(column=0, row=3, sticky=tkinter.N + tkinter.E + tkinter.W + tkinter.S)

km_label = Label(text=" Km", font=("", 14), anchor="w")
km_label.grid(column=6, row=3, sticky=tkinter.N + tkinter.E + tkinter.W + tkinter.S)

convert = Button(text="Convert", font=("", 16), width=8, command=convert)
convert.grid(column=0, row=4, pady=15)

window.mainloop()
