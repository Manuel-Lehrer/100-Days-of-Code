from tkinter import *

def button_clicked():
    output["text"] = round(float(input.get())*1.609, 2)

#window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

#Label
my_label = Label(text="Miles", font=("Arial", 24))
my_label.grid(row=0, column=2)

my_label1 = Label(text="is equal to", font=("Arial", 24))
my_label1.grid(row=1, column=0)

my_label2 = Label(text="Km", font=("Arial", 24))
my_label2.grid(row=1, column=2)

output = Label(text="0", font=("Arial", 24))
output.grid(row=1, column=1)

#Button
button = Button(text ="Calculate", command= button_clicked)
button.grid(row=2, column=1)


#Entry
input = Entry(width=20)
input.grid(row=0, column=1)




window.mainloop()