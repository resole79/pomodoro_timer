from tkinter import *
from PIL import Image
from playsound import playsound

# Declare variable and CONSTANT
IMAGE = "./image/tomato.png"
# IMAGE = "./image/batman.png"

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_marker = ""
reps = 8
timer = 0

# Get size of image
open_image = Image.open(IMAGE)
width, height = open_image.size


# Function to reset timer
def timer_reset():
    """Function to reset timer"""
    global reps
    window.after_cancel(timer)
    canv.itemconfig(text_timer, text="00:00")
    reps = 0
    timer_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"))
    checkbox.config(text="")
    start_button.config(state="normal")


# Function to start timer
def timer_start():
    """Function to start timer"""
    global reps
    reps += 1
    long_sec = LONG_BREAK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    work_sec = WORK_MIN * 60

    start_button.config(state="disabled")
    if reps % 8 == 0:
        count_down(long_sec)
        timer_label.config(text="Long Break Time", fg=RED, font=(FONT_NAME, 18, "bold"))
    elif reps % 2 == 0:
        count_down(short_sec)
        timer_label.config(text="Short Break Time", fg=PINK, font=(FONT_NAME, 18, "bold"))
    else:
        count_down(work_sec)
        timer_label.config(text="Work Time", fg=GREEN, font=(FONT_NAME, 18, "bold"))


# Function to count down timer
def count_down(count):
    """Function to count down timer"""
    global timer, check_marker
    count_min = count // 60
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canv.itemconfig(text_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        timer_start()

        check_marker = ""
        mark = reps//2
        for _ in range(mark):
            check_marker += "✓"
            checkbox.config(text=check_marker)
        playsound('./sound/alarm.mp3')


# Create window object
window = Tk()

window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

# Create Label "timer"
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

# Create Canvas object
canv = Canvas(width=width, height=height, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file=IMAGE)
canv.create_image(width//2, height//2, image=tomato_image)
text_timer = canv.create_text(110, 150, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canv.grid(column=1, row=1)

# Create buttons object
start_button = Button(text="Start Timer", highlightthickness=0, command=timer_start)
start_button.grid(column=0, row=3)

end_button = Button(text="Reset Timer", highlightthickness=0,  command=timer_reset)
end_button.grid(column=2, row=3)

# Create Label "checkbox"
checkbox = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkbox.grid(column=1, row=4)

window.mainloop()
