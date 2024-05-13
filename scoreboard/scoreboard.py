class Scoreboard():
    def __init__(self):
        self.score = 0
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.score)

    def increase_score(self, points):
        self.score += points
        self.notify_observers()

    def reset_score(self):
        self.score = 0
        self.notify_observers()