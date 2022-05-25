from utils.printable import Printable
from time import time


class Interest(Printable):
    def __init__(self, interests, now=None) -> None:
        self.interests = interests
        self.timestamp = time() if now is None else now