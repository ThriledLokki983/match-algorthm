from utils.goal import Goal
from utils.interest import Interest
from pickle import dump, load
import json
from colorama import Fore
from utils.encoder import Encoder


class Criteria:
    def __init__(self, profile) -> None:
        self.id = profile.profile_id
        self.profile = profile
        self.goals = []
        self.interests = []
        self.profiles = []

    def get_user_choice(self):
        return input('Your choice: ')

    def show_goals(self):
        print(Fore.BLUE + 'Select a goal from the list below:')
        print('1: Getting to know new communities in PwC')
        print('2: Working more x-LoS with PwC')
        print('3: Fostering an inclusive working environment')
        print('q: Continue!')

    def show_interests(self):
        print(Fore.YELLOW + 'Select an interest from the list below:')
        print('1: Home')
        print('2: Movies')
        print('3: Sports and outdoors')
        print('4: Meditation')
        print('5: Scaleups')
        print('q: Continue!')

    def get_goals(self) -> None:
        show_available_goals = True

        while show_available_goals:
            self.show_goals()
            user_choice = self.get_user_choice()
            if user_choice == '1':
                self.goals.append('Getting to know new communities in PwC')
            elif user_choice == '2':
                self.goals.append('Working more x-LoS with PwC')
            elif user_choice == '3':
                self.goals.append('Fostering an inclusive working environment')
            elif user_choice == 'q':
                self.profile.set_goals(goals=self.goals)
                # print(self.profile.__dict__)
                show_available_goals = False
        else:
            print(Fore.BLUE + 'Goals added!')
        print('Done!')

    def get_interests(self) -> None:
        show_available_interest = True

        while show_available_interest:
            self.show_interests()
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
            print(Fore.YELLOW + 'Interests added!')
        print('Done!')

    def save_data(self) -> None:
        try:
            if self.id is not None:
                with open('goals-interests-profiles.txt', 'a') as file:
                    if len(self.profile.goals.goals) > 0 and len(self.profile.interests.interests) > 0:
                        file.write(
                            json.dumps(Encoder().encode(self.profile.to_ordered_dict()), indent=4))
            else:
                print(Fore.RED + "No profile found")
        except IOError:
            print(Fore.RED + 'Error: Could not save data to file.')

    def get_user_choice(self):
        return input('Your choice: ')

    def menu(self):
        self.get_goals()
        self.get_interests()
        self.save_data()
