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

window.bind('<KeyPress-Left>', platform.start_left)
window.bind('<KeyRelease-Left>', platform.stop_left)
window.bind('<KeyPress-Right>', platform.start_right)
window.bind('<KeyRelease-Right>', platform.stop_right)

while True:
    if not ball.touch_bottom:
        ball.draw()
        platform.move()
    else:
        ball = Ball(canvas, platform, scoreboard, 'red')
        scoreboard.reset_score()  # Скидання рахунку до нуля
    window.update()
    time.sleep(0.01)

window.mainloop()