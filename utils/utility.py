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
        except (IOError, IndexError):
            print(Fore.RED + 'Error: Could not load data from file.')
    
    def save_data(self, profile) -> None:
        print(profile.__dict__)
        if profile.profile_id is not None:
            try:
                with open('goals-interests-profiles.txt', 'a') as file:
                    try:
                        if len(profile.__dict__['goals'].goals) > 0 and len(profile.__dict__['interests'].interests) > 0:
                            file.write(jsonpickle.encode(profile) + '\n')
                        else:
                            print(Fore.RED + 'Error: No profile found or there are no goals/interests')
                    except (KeyError, AttributeError):
                        print(Fore.RED + 'Error: No profile found or there are no goals/interests')
            except IOError:
                print(Fore.RED + 'Error: Could not save data to file.')
