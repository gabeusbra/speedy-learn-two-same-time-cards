import random
from tkinter import *
from tkinter import Button
from gtts import gTTS
import pandas
import pygame
import os
base_dir = os.path.dirname(__file__)


BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}
current_card = {}
changeIt = {}

try:
    data = pandas.read_csv(base_dir+"/data/wordsToLearn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(base_dir+"/data/IT-FR-EN.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



initialLoad = True;
def randomly():
    currentCard = random.choice(to_learn)
    global changeIt
    changeIt = currentCard


if initialLoad:
    randomly()

def next_card():
    global current_card, flipTimer
    window.after_cancel(flipTimer)

    if not initialLoad:
        randomly()
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_title2, text="Italian")

    canvas.itemconfig(card_word, text=changeIt["French"], fill="black")
    canvas.itemconfig(card_word2, text=changeIt["Italian"])
    speech('fr', changeIt["French"])
    speech('it', changeIt["Italian"])
    canvas.itemconfig(card_background, image=card_front_img)
    speech_symbol_button2 = Button(image=speech_symbol2, highlightthickness=0, command=lambda: play(2), borderwidth=0,
                                   bd=0)
    speech_symbol_button2.place(x=550, y=290)
    speech_symbol_button.config(command=lambda: play(1))

    play('1')
    flipTimer = window.after(7000, func=flip_card)


def speech(lang, text):
    language = lang
    speechIt = gTTS(text=text,
                    lang=lang,
                    slow=False)
    if lang == 'fr':
        speechIt.save(base_dir+"/audios/audio1.mp3")
    elif lang == 'it':
        speechIt.save(base_dir+"/audios/audio2.mp3")
    else:
        speechIt.save(base_dir+"/audios/audio3.mp3")

def play(file):
    file = str(file)

    pygame.mixer.init()  # initialize mixer module
    pygame.mixer.music.load(base_dir+'/audios/audio'+file+'.mp3')

    pygame.mixer.music.play()
    print(changeIt)



def flip_card():

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_title2, text="")
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_word, text=changeIt["English"], fill="white")
    canvas.itemconfig(card_word2, text="")
    speech_symbol_button2.config(command=play(1))
    speech('en', changeIt["English"])
    speech_symbol_button.config(command=lambda: play(3))
    play('3')

def isKnown():
    to_learn.remove(changeIt)
    print((len(to_learn)))
    data = pandas.DataFrame(to_learn)
    data.to_csv(base_dir+"/data/wordsToLearn.csv", index=False)

    next_card()

window = Tk()
window.title("Flashy Languages")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flipTimer = window.after(7000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file=base_dir+"/images/card_front.png")
card_back_img = PhotoImage(file=base_dir+"/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_title2 = canvas.create_text(400, 185, text="[Title 2]", font=("Ariel", 24, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))


speech_symbol = PhotoImage(file=base_dir+"/images/sound42x42.png")
speech_symbol_button = Button(image=speech_symbol, highlightthickness=0, command=lambda: play(1), borderwidth=0, bd=0)
speech_symbol_button.place(x=550, y=240)

card_word2 = canvas.create_text(400, 303, text="[word 2]", font=("Ariel", 35, "bold"))

speech_symbol2 = PhotoImage(file=base_dir+"/images/soundSmall.png")
speech_symbol_button2 = Button(image=speech_symbol2, highlightthickness=0, command=lambda: play(2), borderwidth=0, bd=0)
speech_symbol_button2.place(x=550, y=290)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file=base_dir+"/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card, borderwidth=0, bd=0)
unknown_button.grid(row=1, column=0)



check_image = PhotoImage(file=base_dir+"/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=isKnown, borderwidth=0)
known_button.grid(row=1, column=1)

next_card()
initialLoad = False;
window.mainloop()
