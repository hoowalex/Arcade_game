class Platform():
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
        self.x = 0
        self.move_left = False
        self.move_right = False
        self.canvas.bind_all('<KeyPress-Left>', self.start_left)
        self.canvas.bind_all('<KeyRelease-Left>', self.stop_left)
        self.canvas.bind_all('<KeyPress-Right>', self.start_right)
        self.canvas.bind_all('<KeyRelease-Right>', self.stop_right)

    def start_left(self, event):
        self.move_left = True

    def stop_left(self, event):
        self.move_left = False

    def start_right(self, event):
        self.move_right = True

    def stop_right(self, event):
        self.move_right = False

    def move(self):
        if self.move_left:
            if self.canvas.coords(self.rect)[0] > 0:  # Перевірка, чи платформа не виходить за межі вікна
                self.x = -2
            else:
                self.x = 0
        elif self.move_right:
            if self.canvas.coords(self.rect)[2] < 500:  # Перевірка, чи платформа не виходить за межі вікна
                self.x = 2
            else:
                self.x = 0
        else:
            self.x = 0
        self.canvas.move(self.rect, self.x, 0)

 # type: ignore