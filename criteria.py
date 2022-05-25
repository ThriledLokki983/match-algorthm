from operator import truediv
import jsonpickle
from colorama import Fore
from utils.encoder import Encoder
from match import Match


class Criteria:
    def __init__(self, profile) -> None:
        self.id = profile.profile_id
        self.profile = profile
        self.goals = []
        self.interests = []
        self.profiles = []
        self.match = None
        self.goal_list = ['Getting to know new communities in PwC',
                          'Working more x-LoS with PwC', 'Fostering an inclusive working environment']
        self.interest_list = ['Home', 'Movies',
                              'Sports and outdoors', 'Meditation', 'Scaleups']

    def get_user_choice(self):
        return input('Your choice: ')

    def show_data(self, list, title):
        print(Fore.BLUE + 'Select a {} from the list below:'.format(title))
        for i, item in enumerate(list):
            print(Fore.BLUE + '{}: {}'.format(i+1, item))
        print('q: Continue!')
        print("=" * 50 + '\n')

    def get_goals(self) -> None:
        show_available_goals = True

        while show_available_goals:
            self.show_data(list=self.goal_list, title='goal')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                self.goals.append('Getting to know new communities in PwC')
            elif user_choice == '2':
                self.goals.append('Working more x-LoS with PwC')
            elif user_choice == '3':
                self.goals.append('Fostering an inclusive working environment')
            elif user_choice == 'q':
                self.profile.set_goals(goals=self.goals)
                show_available_goals = False
        else:
            print(Fore.GREEN + 'Goals added!' + '\n')
        # print('Done!' + '\n')

    def get_interests(self) -> None:
        show_available_interest = True

        while show_available_interest:
            self.show_data(list=self.interest_list, title='interests')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                self.interests.append('Home')
            elif user_choice == '2':
                self.interests.append('Movies')
            elif user_choice == '3':
                self.interests.append('Sports and outdoors')
            elif user_choice == '4':
                self.interests.append('Meditation')
            elif user_choice == '5':
                self.interests.append('Scaleups')
            elif user_choice == 'q':
                self.profile.set_interests(interests=self.interests)
                show_available_interest = False
        else:
            print(Fore.GREEN + 'Interests added!' + '\n')
        # print('Done!' + '\n')

    def save_data(self) -> None:
        try:
            if self.id is not None:
                with open('goals-interests-profiles.txt', 'a') as file:
                    if len(self.profile.goals.goals) > 0 and len(self.profile.interests.interests) > 0:
                        file.write(jsonpickle.encode(
                            self.profile) + '\n')
            else:
                print(Fore.RED + "No profile found")
        except IOError:
            print(Fore.RED + 'Error: Could not save data to file.')

    def show_matching_options(self):
        print(Fore.BLUE + 'Select a matching option:')
        print('1: Print profile details')
        print('2: Start matching')
        print('3: print matching results')
        print('q: Exit')

    def get_user_choice(self):
        return input('Your choice: ')

    def begin_matching(self) -> None:
        matching = True
        
        while matching:
            self.show_matching_options()
            user_choice = self.get_user_choice()
            if user_choice == '1':
                print(self.profile.__dict__)
            elif user_choice == '2':
                self.match = Match(self.profile)
                self.match.start_match()
            elif user_choice == '3':
                self.profile.match()
            elif user_choice == 'q':
                matching = False

    def menu(self):
        self.get_goals()
        self.get_interests()
        self.save_data()
        self.begin_matching()
