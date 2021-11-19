import tkinter
import math
# colorhunt.co is a good website to get color palettes #
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = '✔'
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    if reps in (1, 3, 5, 7):
        # count_down(WORK_MIN * 60)
        count_down(10)
    elif reps in (2, 4, 6):
        # count_down(SHORT_BREAK_MIN * 60)
        count_down(5)
    else:
        count_down(LONG_BREAK_MIN * 60)
        reps = 0
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(duration):
    global reps
    display_time = str(math.trunc(duration / 60)).zfill(2) + ':' + str(duration % 60).zfill(2)
    canvas.itemconfig(timer_text, text=display_time)
    if duration > 0:
        window.after(1000, count_down, duration-1)
    else:
        print('')
        # if reps % 2 == 0:
        #     print('what')
        # start_timer()
        # TODO: write check


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=80, pady=35, bg=YELLOW)

lbl_timer = tkinter.Label(text="Timer", font=(FONT_NAME, 35, 'normal'), bg=YELLOW, fg=GREEN)
lbl_timer.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img_tomato = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(101, 112, image=img_tomato)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

btn_start = tkinter.Button(width=2, height=1, text='Start', command=start_timer)
btn_start.grid(column=0, row=2)

btn_reset = tkinter.Button(width=2, height=1, text='Reset')
btn_reset.grid(column=2, row=2)

lbl_completions = tkinter.Label(text=CHECK, font=(FONT_NAME, 24, 'bold'), bg=YELLOW, fg=GREEN)
lbl_completions.grid(column=1, row=3)


window.mainloop()