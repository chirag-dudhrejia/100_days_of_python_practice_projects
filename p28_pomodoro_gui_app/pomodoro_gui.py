from tkinter import *
from PIL import Image, ImageTk

# Constants
YELLOW = "#F6FDC3"
GREEN = "#9BCF53"
ORANGE = "#FFCF96"
RED = "#FF8080"
FONT = "Courier"
WORK_MIN = 0.25
SHORT_BREAK = 0.10
LONG_BREAK = 0.20
reps = 0
timer = ""
#-------------------------------------------------------------------------------------------------------------------

window = Tk()
window.title("Pomodoro GUI")
window.minsize(300, 450)
window.resizable(False, False)
window.config(bg=YELLOW, padx=80, pady=50)

# Center Window
win_width = 450
win_height = 450
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int(screen_width/2 - win_width/2)
y = int(screen_height/2 - win_width/2)
window.geometry(f"{win_width}x{win_height}+{x}+{y}")

ico = Image.open("tomato.png")
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)


# Reset Timer
def reset_timer():
    reset_button.grid_forget()
    start_button.grid(column=1, row=2, pady=10)
    global timer, reps
    reps = 0
    window.after_cancel(timer)
    timer = ""
    canvas.itemconfig(timer_text, text="00:00")
    activity_label.config(text="Work", fg=GREEN)
    check_mark.config(text="")
    start_button.config(state="active")


# Start Timer
def start_timer():
    # start_button.config(state="disabled", disabledforeground=start_button["foreground"])
    start_button.grid_forget()
    reset_button.grid(column=1, row=2, pady=10)
    global reps
    reps += 1

    if reps > 8:
        window.bell()
        return
    work_secs = 15
    short_break_secs = 5
    long_break_secs = 10

    window.attributes("-topmost", 1)
    window.attributes("-topmost", 0)
    window.state("normal")

    if reps % 8 == 0:
        count_down(long_break_secs)
        activity_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        activity_label.config(text="Short Break", fg=RED)
    else:
        count_down(work_secs)
        activity_label.config(text="Work", fg=GREEN)

    # window.bell()


# Countdown each task
def count_down(count):

    count_mins = count // 60
    count_secs = count % 60

    if count_secs < 10:
        count_secs = f"0{count_secs}"

    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(200, count_down, count-1)
    else:
        start_timer()
        check_mark.config(text="✔" * (reps//2))


# Activity label (Work, Short break, Long Break)
activity_label = Label(text="Work", fg=GREEN, width=15, font=(FONT, 24, "bold"), bg=YELLOW)
activity_label.grid(column=1, row=0)

# Tomato image
tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)

# Timer Text
timer_text = canvas.create_text(105, 130, text="00:00", font=(FONT, 24, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Start Button
start_button = Button(text="Start", bg=GREEN, font=("FONT", 14), width=10, command=start_timer)
start_button.grid(column=1, row=2, pady=10)

# Reset Button
reset_button = Button(text="Reset", bg=RED, font=("FONT", 14), width=10, command=reset_timer)

# Check Mark "✔"
check_mark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT, 20))
check_mark.grid(column=1, row=3)

window.mainloop()
