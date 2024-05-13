from moving.command import Command

class MoveLeftCommand(Command):
    def __init__(self, platform):
        self.platform = platform
    
    def execute(self):
        self.platform.move_left()