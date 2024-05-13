from speed_moving_change.speed_strategy import SpeedStrategy

class HighSpeedStrategy(SpeedStrategy):
    def increase_speed(self, ball):
        ball.speed_x *= 1.3
        ball.speed_y *= 1.3