import json
from interface import Interface


class Application:
    def __init__(self):
        self.profiles = []
        self.interface = Interface()
        self.load_profiles()

    def load_profiles(self):
        with open('goals-interests-profiles.txt', 'r') as file:
            f_content = file.readlines()
            self.profiles.append(json.loads(file) for file in f_content)
        print(self.profiles)


app = Application()
