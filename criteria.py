from operator import truediv
import sys
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
        self.account_data = []
        self.profiles = []
        self.selected_options = []
        self.match = None
        self.goal_list = ['Getting to know new communities in PwC',
                          'Working more x-LoS with PwC', 'Fostering an inclusive working environment']
        self.interest_list = ['Home', 'Movies',
                              'Sports and outdoors', 'Meditation', 'Scaleups']
        self.account_info_list = ['Management Level', 
                                  'Start year', 'Gender', 'Birth year']

    def get_user_choice(self):
        return input('Your choice: ')
    
    def add_account_data(self, index):
        if int(index) not in self.selected_options and len(self.selected_options) != 4:
            user_input = input(Fore.CYAN + self.account_info_list[index-1] + ': ')
            self.account_data.insert(index, user_input)
            self.selected_options.append(index)
        else:
            print(Fore.RED + 'Option [ {} ] has already been selected!'.format(index))
            return
    
    def add_goal_data(self, index):
         if int(index) not in self.selected_options:
             pass
        
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
                self.profile.set_goals(data=self.goals)
                show_available_goals = False
        else:
            print(Fore.GREEN + 'Goals added!' + '\n')
        
    def get_account_data(self) -> None:
        show_available_account_data = True
        while show_available_account_data:
            self.show_data(list=self.account_info_list, title='account_data')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                self.add_account_data(1)
            elif user_choice == '2':
                self.add_account_data(2)
            elif user_choice == '3':
                self.add_account_data(3)
            elif user_choice == '4':
                self.add_account_data(4)
            elif user_choice == 'q' or len(self.selected_options) == 4:
                self.profile.set_up_account(data=self.account_data)
                show_available_account_data = False
                self.selected_options = []
            else:
                print(Fore.RED + 'Option not recognized, please select from list below! or from [1, 2, 3, 4, q]')
                continue
        else:
             print(Fore.GREEN + 'Account set up is completed!' + '\n')
            
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
                self.profile.set_interests(data=self.interests)
                show_available_interest = False
        else:
            print(Fore.GREEN + 'Interests added!' + '\n')

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

    def show_matching_options(self) -> None:
        print(Fore.BLUE + 'Select a matching option:')
        print('1: Print profile details')
        print('2: Start single profile matching')
        print('3: Recalculate profile matching')
        print('4: print matching results')
        print('q: Exit')

    def begin_matching(self) -> None:
        matching = True
        
        while matching:
            try:
                self.show_matching_options()
                user_choice = self.get_user_choice()
                if user_choice == '1':
                    print(self.profile.__dict__)
                elif user_choice == '2':
                    self.match = Match()
                    self.match.start_single_profile_match(profile=self.profile)
                elif user_choice == '3':
                    self.match.check_matches_for_all_profiles()
                elif user_choice == '4':
                    self.profile.match()
                elif user_choice == 'q':
                    matching = False
            except (ValueError, TypeError, AttributeError):
                print(Fore.RED + 'Error: Invalid input')
                # print the error message
                print(sys.exc_info()[0])
                continue

    def menu(self) -> None:
        self.get_account_data()
        self.get_goals()
        self.get_interests()
        print(self.profile.__dict__)
        self.save_data()
        self.begin_matching()


# cri = Criteria()
# cri.menu()