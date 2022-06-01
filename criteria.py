from operator import truediv
import sys
import jsonpickle
from colorama import Fore
from match import Match
from utils.utility import Utility


class Criteria(Utility):
    def __init__(self, profile) -> None:
        super().__init__()
        self.show_available_data = True
        self.id = profile.profile_id
        self.profile = profile
        self.goals = []
        self.interests = []
        self.account_data = []
        self.profiles = []
        self.selected_options = []
        self.match = None
        self.goal_list = ['Fostering an inclusive working environment',
                          'Looking for a better fit on my skills and talent',
                          'Maintaining relationships',
                          'Boosting my wellbeing & mental health',
                          'Making my work more meaningful',
                          'Joining a group',
                          'Finding people to join my group',
                          'Making my work more social and fun',
                          'Working with different people',
                          'Working more x-LoS',
                          'Getting new opportunities',
                          'Gaining visibility',
                          'Achieving career development goal',
                          'Being mentored',
                          'Getting advised',
                          'Needing help',
                          'Gaining new knowledge',
                          'Getting to know new communities in PwC',
                          'Being more open to new viewpoints'
                          ]
        self.interest_list = ['Scaleups', 'Startups', 'Yoga', 'Weight training', 'Running',
                              'Physical fitness', 'Physical exercise', 'Meditation', 'Bodybuilding',
                              'Sports and outdoors', 'Outdoor recreation', 'Movies', 'Live events', 
                              'Games', 'Vehicles', 'Travel', 'Social issues', 'Politics', 
                              'Pets', 'Garden', 'Home', 'Music', 'Arts'  
                              ]
        self.account_info_list = ['Management Level', 'Start year', 'Gender', 'Birth year']

    def get_user_choice(self):
        return input('Your choice: ')

    def add_profile_data(self, data=None, profile_data=None, account=False):
        index = self.get_user_choice()
        if account is True:
            try: 
                if int(index) not in self.selected_options and len(self.selected_options) != len(data):
                    user_input = input(Fore.CYAN + data[int(index) - 1] + ': ')
                    if profile_data is not None:
                        profile_data.insert(int(index), user_input)
                    self.selected_options.append(int(index))
                else:
                    print(Fore.RED + 'Option [ {} ] has already been selected!'.format(index))
                    return
            except ValueError:
                return
        else:
            selected_option = int(index) - 1
            profile_data.insert(selected_option, data[selected_option])
            # print(f'{Fore.CYAN}You have selected: {data[int(index) - 1]}')
            print(profile_data)

    def add_goal_data(self, index):
        if int(index) not in self.selected_options:
            pass

    def show_data(self, item_list, title, data=None, account=False):
        print(Fore.BLUE + f'Select a {title} from the list below:')
        for i, item in enumerate(item_list):
            print(Fore.BLUE + '{}: {}'.format(i + 1, item))
        print('q: Continue!')
        print("=" * 50 + '\n')
        self.add_profile_data(data=item_list, profile_data=data, account=account)

    def get_account_data(self) -> None:
        while len(self.account_data) != len(self.account_info_list):
            self.show_data(item_list=self.account_info_list, title='account_data', data=self.account_data, account=True)
        
    def get_goals(self) -> None:
        while len(self.goals) <= 3:
            self.show_data(item_list=self.goal_list, title='goal')
        #     user_choice = self.get_user_choice()
        #     if user_choice == '1':
        #         self.goals.append('Getting to know new communities in PwC')
        #     elif user_choice == '2':
        #         self.goals.append('Working more x-LoS with PwC')
        #     elif user_choice == '3':
        #         self.goals.append('Fostering an inclusive working environment')
        #     elif user_choice == 'q':
        #         self.profile.set_goals(data=self.goals)
        #         show_available_goals = False
        # else:
        #     print(Fore.GREEN + 'Goals added!' + '\n')


    def get_interests(self) -> None:
        show_available_interest = True

        while show_available_interest:
            self.show_data(item_list=self.interest_list, title='interest')
        #     user_choice = self.get_user_choice()
        #     if user_choice == '1':
        #         self.interests.append('Home')
        #     elif user_choice == '2':
        #         self.interests.append('Movies')
        #     elif user_choice == '3':
        #         self.interests.append('Sports and outdoors')
        #     elif user_choice == '4':
        #         self.interests.append('Meditation')
        #     elif user_choice == '5':
        #         self.interests.append('Scaleups')
        #     elif user_choice == 'q':
        #         self.profile.set_interests(data=self.interests)
        #         show_available_interest = False
        # else:
        #     print(Fore.GREEN + 'Interests added!' + '\n')

    def show_matching_options(self) -> None:
        print(Fore.BLUE + 'Select a matching option:')
        print('1: Print profile details')
        print('2: Start single profile matching')
        print('3: Recalculate profile matching')
        print('4: print complete profile details')
        print('q: Exit')

    def begin_matching(self) -> None:
        matching = True
        self.match = Match()
        # Recalculate the profile matching score right after the profile is created for all profiles in the database
        self.match.check_matches_for_all_profiles()
        
        while matching:
            try:
                self.show_matching_options()
                user_choice = self.get_user_choice()
                if user_choice == '1':
                    print(("=" * 100))
                    print(self.match.get_profile_data(profile_id=self.id))
                    print(("=" * 100) + '\n')
                elif user_choice == '2':
                    self.match.start_single_profile_match(profile=self.profile)
                elif user_choice == '3':
                    self.match.check_matches_for_all_profiles()
                elif user_choice == '4':
                    self.match.get_matched_profiles_data()
                elif user_choice == 'q':
                    matching = False
            except (ValueError, TypeError, AttributeError):
                print(Fore.RED + 'Error: Invalid input')
                continue

    def menu(self) -> None:
        self.get_account_data()
        self.get_goals()
        self.get_interests()
        self.save_data(self.profile)
        self.begin_matching()

# cri = Criteria()
# cri.menu()
