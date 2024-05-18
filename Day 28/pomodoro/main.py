from tkinter import *
import playsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE


def play_sound():
    sound_file = "Break.mp3"
    playsound.playsound(sound_file)


# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        seconds = LONG_BREAK_MIN * 60
        my_label.config(text="Long Break", fg=RED)
        play_sound()
    elif reps % 2 == 1:
        seconds = WORK_MIN * 60
        my_label.config(text="Work")
    else:
        seconds = SHORT_BREAK_MIN * 60
        my_label.config(text="Short Break", fg=PINK)
        play_sound()

    count_down(seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = int(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        marks = ""
        work_sessions = int(reps / 2)
        for i in range(work_sessions):
            marks += "✔"
        checkmarks.config(text=marks),


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

window.after(1000, )


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


my_label = Label(text="Timer", font=(FONT_NAME, 34, "bold"), fg=GREEN, bg=YELLOW)
my_label.grid(row=0, column=1)

checkmarks = Label(font=("Arial", 24), fg=GREEN, bg=YELLOW)
checkmarks.grid(row=3, column=1)

start_button = Button(text="Start", font=("Arial", 12), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=("Arial", 12), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()
