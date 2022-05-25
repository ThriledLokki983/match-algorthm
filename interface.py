from citeria import Criteria
from profile import Profile
from colorama import Fore


class Interface:
    def __init__(self) -> None:
        self.running = True
        self.profile_id = None
        self.criteria = None
        self.profile = Profile()
        self.yes = ['y', 'Y', 'yes', 'Yes', 'YES']
        self.menu()

    def create_profile(self) -> None:
        """
        Create a new profile.
        """
        self.profile_id = self.profile.create_profile()
        self.criteria = Criteria(self.profile)
        print('New profile created: {}'.format(self.profile_id))

    def menu(self):
        """
        CLI Interface for the program, where users will make choices to actively interact with the program.
        """
        while self.running:
            print('Application initialized')
            if self.profile_id is None:
                print(Fore.RED + 'No profile found. Create a new profile?')
                user_choice = input(Fore.CYAN + 'y/n: ')
                if user_choice in self.yes:
                    self.create_profile()
                    self.criteria.menu()
                    self.running = False
                elif user_choice == 'n':
                    print(Fore.LIGHTGREEN_EX + 'Exiting...')
                    self.running = False
                else:
                    print(Fore.RED + 'Invalid input. Exiting...')
                    self.running = False
