class Platform():
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
        self.x = 0

    def move_left(self):
        if self.canvas.coords(self.rect)[0] > 0:
            self.x = -2
        else:
            self.x = 0

    def move_right(self):
        if self.canvas.coords(self.rect)[2] < 500:
            self.x = 2
        else:
            self.x = 0

    def draw(self):
        self.canvas.move(self.rect, self.x, 0)
 # type: ignore