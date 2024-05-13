class Ball():
    def __init__(self, canvas, platform, scoreboard, color):
        self.canvas = canvas
        self.platform = platform
        self.scoreboard = scoreboard
        self.oval = None
        self.speed_x = 3  
        self.speed_y = -3  
        self.touch_bottom = False  

    def create(self):
        self.oval = self.canvas.create_oval(200, 200, 215, 215, fill='red')

    def draw(self):
        self.canvas.move(self.oval, self.speed_x, self.speed_y)
        pos = self.canvas.coords(self.oval)
        if pos[1] <= 0:
            self.speed_y = 3 
        if pos[3] >= 400:
            self.touch_bottom = True  
        if self.touch_platform(pos):
            self.speed_y = -3  
            self.scoreboard.increase_score(1)
        if pos[0] <= 0 or pos[2] >= 500:
            self.speed_x = -self.speed_x  

    def touch_platform(self, ball_pos):
        platform_pos = self.canvas.coords(self.platform.rect)
        if ball_pos[2] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
            if ball_pos[3] >= platform_pos[1] and ball_pos[3] <= platform_pos[3]:
                return True
        return False