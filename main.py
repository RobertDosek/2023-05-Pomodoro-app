from tkinter import *
import math
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
timer = None


# time reset
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    top_label.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0


# timer
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN  * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if it's the 1st/3rd/5th/7th
    if reps % 2 != 0:
        count_down(work_sec)
        top_label.config(text="Work", fg=GREEN)
    # if it's the 8th
    elif reps % 8 == 0:
        count_down(long_break_sec)
        top_label.config(text="Break", fg=RED)
    # if it's the 2nd/4th/6th/
    else:
        count_down(short_break_sec)
        top_label.config(text="Break", fg=PINK)


# countdown mechanism
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_label.config(text=marks)


# UI setup
window =  Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)

top_label = Label(text="Timer",bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
top_label.grid(column=1, row=0)

check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30))
check_label.grid(column=1, row=3)

start_button = Button(text="Start",font=(FONT_NAME, 10),highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",font=(FONT_NAME, 10, "bold"),highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()