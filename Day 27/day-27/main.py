from tkinter import *

def button_clicked():
    my_label["text"] = input.get()

#window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=600, height=600)
window.config(padx=20,pady=20)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)
#Button
button = Button(text ="Click me", command= button_clicked)
button.grid(row=1, column=1)

new_button = Button(text = "Noooo, Click me", command= button_clicked)
new_button.grid(row=0, column=2)


#Entry
input = Entry(width=20)
input.grid(row=2, column=3)




window.mainloop()
