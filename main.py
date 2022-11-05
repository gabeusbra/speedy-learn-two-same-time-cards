import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/IT-FR-EN.csv")
to_learn = data.to_dict(orient="records")



def next_card():
    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_title2, text="Italian")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_word2, text=current_card["Italian"])

window = Tk()
window.title("Flashy Languages")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_title2 = canvas.create_text(400, 185, text="[Title 2]", font=("Ariel", 24, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
card_word2 = canvas.create_text(400, 303, text="[word 2]", font=("Ariel", 35, "bold"))

canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card, borderwidth=0, bd=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card, borderwidth=0)
known_button.grid(row=1, column=1)


next_card()
window.mainloop()