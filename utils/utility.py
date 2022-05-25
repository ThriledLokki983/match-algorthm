import jsonpickle
from colorama import Fore

class Utility:
    def __init__(self):
        self.data = []
        self.load_data()
        
    def load_data(self):
        try:
            with open('goals-interests-profiles.txt', 'r') as file:
                for x in file.readlines():
                    self.data.append(jsonpickle.decode(x).__dict__)
            # print(self.profiles)
        except (IOError, IndexError):
            print(Fore.RED + 'Error: Could not load data from file.')
