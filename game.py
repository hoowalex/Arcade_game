from tkinter import *
from platform import Platform # type: ignore
from record_manager import record_manager
from scoreboard.scoreboard import Scoreboard
from scoreboard.scoreboard_observer import WindowScoreboardObserver
from GameController import  GameController

class Game:
    def __init__(self):
        self.window = Tk()
        self.window.title("Аркада")
        self.window.resizable(0, 0)
        self.window.wm_attributes("-topmost", 1)

        self.canvas = Canvas(self.window, width=500, height=400)
        self.canvas.pack()

        self.platform = Platform(self.canvas, 'blue')
        self.scoreboard = Scoreboard()
        self.window_observer = WindowScoreboardObserver(self.window, self.scoreboard)
        self.scoreboard.add_observer(self.window_observer)

        self.record_label = Label(self.window, text="Рекорд: " + str(record_manager.record))
        self.record_label.pack(side=LEFT)

        self.controller = GameController(self.window, self.canvas, self.platform, self.scoreboard, self.record_label)

    def run(self):
        self.controller.start_game()
        self.window.mainloop()