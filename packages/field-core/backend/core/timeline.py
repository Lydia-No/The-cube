class Timeline:
    def __init__(self, max_len=1000):
        self.history = []
        self.max_len = max_len

    def log(self, state):
        self.history.append(state)
        if len(self.history) > self.max_len:
            self.history.pop(0)

    def latest(self, n=10):
        return self.history[-n:]

    def get(self, idx):
        if idx < 0 or idx >= len(self.history):
            return None
        return self.history[idx]
