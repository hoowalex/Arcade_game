from tkinter import RIGHT, Label

class ScoreboardObserver():
    def update(self, score):
        pass  

class WindowScoreboardObserver(ScoreboardObserver):
    def __init__(self, window, scoreboard):
        self.window = window
        self.scoreboard = scoreboard
        self.score_label = Label(window, text=f"Рахунок: {self.scoreboard.score}")
        self.score_label.pack(side=RIGHT)

    def update(self, score):
        self.score_label.config(text=f"Рахунок: {score}")