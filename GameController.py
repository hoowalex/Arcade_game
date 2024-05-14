import time
from platform import Platform # type: ignore
from ball import Ball
from record_manager import record_manager

class GameController:
    def __init__(self, window, canvas, platform, scoreboard, record_label):
        self.window = window
        self.canvas = canvas
        self.platform = platform
        self.scoreboard = scoreboard
        self.record_label = record_label

        self.window.bind('<KeyPress-Left>', self.platform.start_left)
        self.window.bind('<KeyRelease-Left>', self.platform.stop_left)
        self.window.bind('<KeyPress-Right>', self.platform.start_right)
        self.window.bind('<KeyRelease-Right>', self.platform.stop_right)

    def start_game(self):
        while True:
            ball = Ball(self.canvas, self.platform, self.scoreboard, 'red')
            ball.create()
            while not ball.touch_bottom:
                ball.draw()
                self.platform.move()
                self.window.update()
                time.sleep(0.01)
            self.canvas.delete(ball.oval)
            if self.scoreboard.score > record_manager.record:
                record_manager.update_record(self.scoreboard.score)
                self.record_label.config(text="Рекорд: " + str(record_manager.record))
            self.scoreboard.reset_score()