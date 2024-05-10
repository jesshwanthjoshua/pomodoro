import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1/2
LONG_BREAK_MIN = 3/4
reps = 4
reps_count = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global label_1, reps, reps_count
    window.after_cancel(timer)
    label_1.config(text="TIMER", fg=GREEN, font=(FONT_NAME, 18, "normal"))
    canvas.itemconfig(timer_text, text="00.00")
    check_mark.config(text="")
    reps = 4
    reps_count = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps, reps_count
    reps += 1
    print(reps)

    init_tick = "✔"
    tick = init_tick

    if reps % 2 != 0:
        count_down(WORK_MIN * 60)
        label_1.config(text="WORK", fg= GREEN, font=(FONT_NAME, 18, "bold"))
        reps_count += 1

    elif reps % 2 == 0 and reps != 8:
        count_down(SHORT_BREAK_MIN * 60)
        label_1.config(text="BREAK", fg=PINK)
        reps_count += 1

    else:
        count_down(LONG_BREAK_MIN * 60)
        label_1.config(text="BREAK", fg=RED,  font=(FONT_NAME, 18, "bold"))
        reps_count += 1

    if reps_count == 2:
        reps_count = 0
        check_mark.config(text=tick)
        tick += init_tick
        reps_count = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = round(count % 60)

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count-1)
    elif count == 0:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_1 = Label(text="TIMER", font=(FONT_NAME, 18, "normal"), fg=GREEN,bg=YELLOW)
label_1.grid(column=1, row= 0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)
timer_text = canvas.create_text(100, 115, text="00.00", fill="white", font=(FONT_NAME, 22, "italic"))
canvas.grid(column= 1, row= 2)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3)

check_mark = Label(width=15, height=1, fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=4)

window.mainloop()
