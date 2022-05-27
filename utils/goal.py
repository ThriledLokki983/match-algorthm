from time import time
from utils.printable import Printable


class Goal(Printable):
    def __init__(self, goals) -> None:
        self.goals = goals
