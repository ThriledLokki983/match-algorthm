from time import time
from utils.printable import Printable

class Goal(Printable):
    def __init__(self, goals, now=None) -> None:
        self.goals = goals
        self.timestamp = time() if now is None else now