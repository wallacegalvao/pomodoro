from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start():
    pass


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
label.config()
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomato_img)
canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", command=start)
start.grid(column=0, row=2)

check = Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 24, "bold"))
check.config()
check.grid(column=1, row=3)

reset = Button(text="Reset", command=reset)
reset.grid(column=2, row=2)

window.mainloop()
