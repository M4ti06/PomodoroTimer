import tkinter
import time
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
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmarks_label.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_min = WORK_MIN * 60
    l_b_min = LONG_BREAK_MIN * 60
    s_b_min = SHORT_BREAK_MIN * 60
    if reps % 2 != 0:
        count_down(work_min)
        title_label.config(text="Time for work")
    elif reps == 8:
        count_down(l_b_min)
        title_label.config(text="Long Break", fg=RED)
    else:
        count_down(s_b_min)
        title_label.config(text="Short Break", fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    elif count_min == 0:
        count_min = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        checkmarks_label.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()

window.title("PomodorTimer")
window.config(padx=100, pady=100, bg=YELLOW)


canvas = tkinter.Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
tomato_photo = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_photo)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 45, "bold"))
canvas.grid(row=1, column=1)

reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

title_label = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

checkmarks_label = tkinter.Label(bg=YELLOW)
checkmarks_label.grid(row=3, column=1)

window.mainloop()
