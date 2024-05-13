class Platform():
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
        self.x = 0
        self.move_left = False
        self.move_right = False

    def start_left(self, event):
        self.move_left = True

    def stop_left(self, event):
        self.move_left = False

    def start_right(self, event):
        self.move_right = True

    def stop_right(self, event):
        self.move_right = False

    def move(self):
        if self.move_left and self.canvas.coords(self.rect)[0] > 0:
            self.x = -2
        elif self.move_right and self.canvas.coords(self.rect)[2] < 500:
            self.x = 2
        else:
            self.x = 0
        self.canvas.move(self.rect, self.x, 0)

 # type: ignore