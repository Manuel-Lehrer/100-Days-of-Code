from tkinter import *
from pandas import *
import random
from gtts import gTTS
import os


current_card = {}
to_learn = {}

try:
    new_words = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_words = read_csv("data/thai_words.csv")
    to_learn = original_words.to_dict(orient="records")
else:
    to_learn = new_words.to_dict(orient="records")


def text_to_speech(word):
    tts = gTTS(text=word, lang='th')  # Specify 'th' for Thai language
    tts.save("word.mp3")  # Save the speech as an audio file
    os.system("start word.mp3")  # Play the audio file (for Windows)


def know_word():
    to_learn.remove(current_card)
    data = DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_card()

# -------------------------- CREATE CARDS ----------------------------- #


def back_card():

    canvas.itemconfig(card, image=back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["ENGLISH"], fill="white")
    canvas.itemconfig(word_n, text="")


def new_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    canvas.itemconfig(card, image=front)
    current_card = random.choice(to_learn)

    thai_words = current_card["WORD"]
    thai_words_n = current_card["THAI"]

    text_to_speech(thai_words)

    canvas.itemconfig(language, text="Thai", fill="Green")
    canvas.itemconfig(word, text=thai_words, fill="Green")
    canvas.itemconfig(word_n, text=thai_words_n, fill="Green")
    flip_timer = window.after(3000, func=back_card)


# you could also have created a dictionary from the framework
# and oriented to "records" and used .choice to get a new word

# all of this is unnecessary if you don't have entry's you won't need
# thai_words = words["WORD"].to_list()
# thai_words_n = words["THAI"].to_list()
# english_words = words["ENGLISH"].to_list()
#
# words_dict = {
#     "WORD": thai_words,
#     "THAI": thai_words_n,
#     "ENGLISH": english_words,
# }
#
# words_data = DataFrame(words_dict)


# ---------------------------- UI SETUP ------------------------------- #


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")

flip_timer = window.after(3000, back_card)

canvas = Canvas(width=1000, height=800, highlightthickness=0)
th = PhotoImage(file="images/img.png")
canvas.create_image((500, 400), image=th)

front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
card = canvas.create_image((500, 400), image=front)
language = canvas.create_text(500, 283, text="Thai", fill="black", font=("Ariel", 40, "italic"))

word = canvas.create_text(500, 433, text="กัน", fill="black", font=("Arial", 40, "bold"))

word_n = canvas.create_text(500, 483, text="(kan)", fill="black", font=("Ariel", 25, "bold"))

canvas.grid(row=0, column=0, columnspan=2, rowspan=4)


photo_checkmark = PhotoImage(file="images/right.png")
checkmark = Button(image=photo_checkmark, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR,
                   command=know_word)

checkmark.place(x=250, y=680)

photo_cross = PhotoImage(file="images/wrong.png")
cross = Button(image=photo_cross, borderwidth=0, bg="#FF7E85", command=new_card)
cross.place(x=650, y=680)

new_card()
window.mainloop()
