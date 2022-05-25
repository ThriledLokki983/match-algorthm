from citeria import Criteria
from profile import Profile


class App:
    def __init__(self) -> None:
        self.running = True
        self.profile_id = None
        self.criteria = None
        self.profile = Profile()
        self.menu()
    
    def create_profile(self) -> None:
        """
        Create a new profile.
        """
        self.profile_id = self.profile.create_profile()
        self.criteria = Criteria(self.profile_id)
        print('New profile created: {}'.format(self.profile_id))
    
    def menu(self): 
        """
        CLI Interface for the program, where users will make choices to actively interact with the program.
        """   
        while self.running:
            print('Application initialized')
            if self.profile_id is None:
                print('No profile found. Create a new profile?')
                user_choice = input('y/n: ')
                if user_choice == 'y':
                    self.create_profile()
                    print(self.profile_id)
                    self.criteria.menu()
                    self.running = False
                elif user_choice == 'n':
                    print('Exiting...')
                    self.running = False
                else:
                    print('Invalid input. Exiting...')
                    self.running = False
    

app = App()