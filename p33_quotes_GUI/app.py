from tkinter import *
import requests

root = Tk()
root.title("Quotes")
WIDTH = 400
HEIGHT = 700
x = (root.winfo_screenwidth() // 2) - (WIDTH // 2)
y = (root.winfo_screenheight() // 2) - (HEIGHT // 2)
root.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
root.config(padx=50, pady=50)


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    canvas.itemconfig(quote_text, text=response.json()["quote"])



canvas = Canvas(width=300, height=415)
img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=img)
quote_text = canvas.create_text(150, 207, text="Click on button below to get quote.", width=250, font=("Courier", 18))
canvas.grid(column=0, row=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(column=0, row=1)

root.mainloop()
