class GameState:
    def __init__(self):
        self.playing = True

    def quit(self):
        self.playing = False

    def state(self):
        return self.playing
