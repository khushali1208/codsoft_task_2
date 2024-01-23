from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(scvalue.get())
            scvalue.set(value)
            screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

window = Tk()
window.geometry("644x900")
window.title("Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(window, textvar=scvalue, font="arial 40 bold")
screen.pack(ipadx=15, pady=15)

button_texts = [
    "9", "8", "7", "6", "5", "4", "3", "2", "1", "0",
    "-", "*", "/", "+", "=", "%", ".", "C"
]

row_val, col_val = 0, 0
f = Frame(window, bg="grey")

for text in button_texts:
    b = Button(f, text=text, padx=28, pady=15, font="TimesRoman 25 bold")
    b.grid(row=row_val, column=col_val, padx=22, pady=5)
    b.bind("<Button-1>", click)
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

    f.pack()

window.mainloop()
