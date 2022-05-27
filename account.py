from utils.printable import Printable
from time import time

class Account(Printable):
    def __init__(self, account_data, now=None) -> None:
        self.account = account_data
        self.timestamp = time() if now is None else now
        
        
        
