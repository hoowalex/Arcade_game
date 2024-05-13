from speed_moving_change.speed_strategy import SpeedStrategy

class NormalSpeedStrategy(SpeedStrategy):
    def increase_speed(self, ball):
        ball.speed_x *= 1.1
        ball.speed_y *= 1.1