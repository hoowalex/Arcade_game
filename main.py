from tkinter import *
import time
from ball import Ball
from platform import Platform # type: ignore
from moving.move_left_command import MoveLeftCommand
from moving.move_right_command import MoveRightCommand
from scoreboard.scoreboard import Scoreboard
from scoreboard.scoreboard_observer import WindowScoreboardObserver

window = Tk()
window.title("Аркада")
window.resizable(0, 0)
window.wm_attributes("-topmost", 1)

canvas = Canvas(window, width=500, height=400)
canvas.pack()

platform = Platform(canvas, 'blue')
scoreboard = Scoreboard()  # Ініціалізуємо об'єкт рахунку
window_observer = WindowScoreboardObserver(window, scoreboard)
scoreboard.add_observer(window_observer)

ball = Ball(canvas, platform, scoreboard, 'red')

def on_left(event):
    move_left_command.execute()

def on_right(event):
    move_right_command.execute()

window.bind('<KeyPress-Left>', on_left)
window.bind('<KeyPress-Right>', on_right)

move_left_command = MoveLeftCommand(platform)
move_right_command = MoveRightCommand(platform)

while True:
    if not ball.touch_bottom:
        ball.draw()
        platform.draw()
    else:
        ball = Ball(canvas, platform, scoreboard, 'red')
    window.update()
    time.sleep(0.01)

window.mainloop()