from tkinter import *
import time


window = Tk()

window.title("the_most_dangerous_writing_app.exe")
window.minsize(height=550, width=800)

label = Label(text="The Most DANGEROUS Writing App", font=('arial', 25, ""))
label.place(relx=0.5, rely=0.07, anchor=CENTER)

string = r""" 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+-=[]\;',./{}|:"<>?"""

dedline_time = None


def keypress(event):
    global dedline_time

    def delete():
        if time.time() >= dedline_time:
            text_box.delete(1.0, END)

    if event.char and event.char in string:
        print(event.char)
        dedline_time = time.time() + 5
        text_box.after(5000, delete)


text_box = Text(height=15, width=60, font=('arial', 15, ""))
text_box.place(relx=0.5, rely=0.5, anchor=CENTER)
text_box.bind('<Key>', keypress)


window.mainloop()

