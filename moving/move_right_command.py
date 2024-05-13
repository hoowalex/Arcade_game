from moving.command import Command

class MoveRightCommand(Command):
    def __init__(self, platform):
        self.platform = platform
    
    def execute(self):
        self.platform.move_right()