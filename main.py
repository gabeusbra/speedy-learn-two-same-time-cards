import random
from tkinter import *
from gtts import gTTS
import pandas
import pygame

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/IT-FR-EN.csv")
to_learn = data.to_dict(orient="records")

changeIt = {}
inicialLoad = True;
def randomy():
    current_card = random.choice(to_learn)
    global changeIt
    changeIt = current_card


if(inicialLoad == True):
    randomy()

def next_card():

    if(inicialLoad == False):
        randomy()
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_title2, text="Italian")

    canvas.itemconfig(card_word, text=changeIt["French"])
    canvas.itemconfig(card_word2, text=changeIt["Italian"])

def speech(lang, text):
    language = lang
    speechIt = gTTS(text=text,
                    lang=lang,
                    slow=False)
    if lang == 'fr':
        speechIt.save("audios/audio1.mp3")
    else:
        speechIt.save("audios/audio2.mp3")

def play():
    pygame.mixer.init()  # initialize mixer module
    pygame.mixer.music.load('audios/audio1.mp3')

    pygame.mixer.music.play()
    print(changeIt)

def play2():
    pygame.mixer.init()  # initialize mixer module
    pygame.mixer.music.load('audios/audio2.mp3')

    pygame.mixer.music.play()
    print(changeIt)

window = Tk()
window.title("Flashy Languages")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_title2 = canvas.create_text(400, 185, text="[Title 2]", font=("Ariel", 24, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

speech('fr', changeIt["French"])
speech('it', changeIt["Italian"])
play()
speech_symbol = PhotoImage(file="images/sound42x42.png")
speech_symbol_button = Button(image=speech_symbol, highlightthickness=0, command=play, borderwidth=0, bd=0)
speech_symbol_button.place(x=550, y=240)

card_word2 = canvas.create_text(400, 303, text="[word 2]", font=("Ariel", 35, "bold"))

speech_symbol2 = PhotoImage(file="images/soundSmall.png")
speech_symbol_button2 = Button(image=speech_symbol2, highlightthickness=0, command=play2, borderwidth=0, bd=0)
speech_symbol_button2.place(x=550, y=290)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card, borderwidth=0, bd=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card, borderwidth=0)
known_button.grid(row=1, column=1)

next_card()
inicialLoad = False;
window.mainloop()
