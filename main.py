from tkinter import *
import time
from ball import Ball
from platform import Platform # type: ignore
from scoreboard.scoreboard import Scoreboard
from scoreboard.scoreboard_observer import WindowScoreboardObserver


window = Tk()
window.title("Аркада")
window.resizable(0, 0)
window.wm_attributes("-topmost", 1)

canvas = Canvas(window, width=500, height=400)
canvas.pack()

platform = Platform(canvas, 'blue')
scoreboard = Scoreboard()  
window_observer = WindowScoreboardObserver(window, scoreboard)
scoreboard.add_observer(window_observer)

ball = Ball(canvas, platform, scoreboard, 'red')

while True:
    if ball.touch_bottom == False:
        ball.draw()
        platform.draw()
    else:
        ball = Ball(canvas, platform, scoreboard, 'red')  # Створюємо новий м'яч для гри
    window.update()
    time.sleep(0.01)

window.mainloop()