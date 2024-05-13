from tkinter import *
import time
from platform import Platform # type: ignore
from ball import Ball
from record_manager import record_manager
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

window.bind('<KeyPress-Left>', platform.start_left)
window.bind('<KeyRelease-Left>', platform.stop_left)
window.bind('<KeyPress-Right>', platform.start_right)
window.bind('<KeyRelease-Right>', platform.stop_right)


record_label = Label(window, text="Рекорд: " + str(record_manager.record))
record_label.pack(side=LEFT) 

while True:
    ball = Ball(canvas, platform, scoreboard, 'red')  
    ball.create()
    while not ball.touch_bottom:
        ball.draw()
        platform.move()
        window.update()
        time.sleep(0.01)
    canvas.delete(ball.oval)  
    if scoreboard.score > record_manager.record:
        record_manager.update_record(scoreboard.score)
        record_label.config(text="Рекорд: " + str(record_manager.record))
    scoreboard.reset_score()

window.mainloop()