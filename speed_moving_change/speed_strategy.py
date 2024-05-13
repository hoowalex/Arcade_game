class SpeedStrategy:
    def increase_speed(self, ball):
        pass

class NormalSpeedStrategy(SpeedStrategy):
    def increase_speed(self, ball):
        ball.speed_x *= 1.1
        ball.speed_y *= 1.1

class HighSpeedStrategy(SpeedStrategy):
    def increase_speed(self, ball):
        ball.speed_x *= 1.5
        ball.speed_y *= 1.5