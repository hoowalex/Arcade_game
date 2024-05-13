from speed_moving_change.speed_strategy import SpeedStrategy

class ExtremeSpeedStrategy(SpeedStrategy):
    def increase_speed(self, ball):
        ball.speed_x *= 1.5
        ball.speed_y *= 1.5