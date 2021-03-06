from colorama import Fore
from match import Match
from utils.utility import Utility


class Criteria(Utility):
    # def __init__(self, profile) -> None:
    def __init__(self) -> None:
        super().__init__()
        self.show_available_data = True
        # self.id = profile.profile_id
        # self.profile = profile
        self.goals = []
        self.interests = []
        self.account_data = []
        self.profiles = []
        self.selected_options = []
        self.matrix_checklist = []
        self.match = None
        self.goal_list = ['Learning PwC tips & tricks',
                          'Sharing PwC tips & tricks',
                          'Connecting with other new joiners',
                          'Connecting with peers',
                          'Finding a buddy to hang out with',
                          'Learning about general expectations related to my grade',
                          'Helping new colleagues to understand PwC',
                          'Learning from new perspectives',
                          'Learn about different specialisms in deals',
                          'Finding a mentor',
                          'Find a mentee',
                          'Learn about a new market',
                          'Share knowledge about my market',
                          'Sharing work experiences',
                          'Finding people working on interesting projects',
                          'Meeting people that could join my project',
                          'Learning about networks/initiatives within the firm',
                          'Finding people to join my network/group',
                          'Learning technical skills',
                          'Helping people to learn technical skills',
                          'Boosting my wellbeing & mental health',
                          'Looking for a better fit on my skills and talent'
                          ]
        self.interest_list = ['Scaleups', 'Startups', 'Yoga', 'Weight training', 'Running',
                              'Physical fitness', 'Physical exercise', 'Meditation', 'Bodybuilding',
                              'Sports and outdoors', 'Outdoor recreation', 'Movies', 'Live events', 
                              'Games', 'Vehicles', 'Travel', 'Social issues', 'Politics', 
                              'Pets', 'Garden', 'Home', 'Music', 'Arts'  
                              ]
        self.account_info_list = ['Management Level', 'Start year', 'Gender', 'Birth year']
        self.matrix = [
        ['Learning PwC tips & tricks', 'Sharing PwC tips & tricks', 'Connecting with other new joiners', 'Connecting with peers', 'Finding a buddy to hang out with', 'Learning about general expectations related to my grade', 'Helping new colleagues to understand PwC ', 'Learning from new perspectives', 'Learn about different specialisms in deals', 'Finding a mentor', 'Find a mentee', 'Learn about a new market', 'Share knowledge about my market', 'Sharing work experiences', 'Finding people working on interesting projects', 'Meeting people that could join my project', 'Learning about networks/initiatives within the firm', 'Finding people to join my network/group', 'Learning technical skills', 'Helping people to learn technical skills', 'Boosting my wellbeing & mental health', 'Looking for a better fit on my skills and talent'],
        ['Learning PwC tips & tricks', True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        ['Sharing PwC tips & tricks', False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        ['Connecting with other new joiners', False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        ['Connecting with peers', False, False, False, True, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        ['Finding a buddy to hang out with', False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False],
        ['Learning about general expectations related to my grade', False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        ['Helping new colleagues to understand PwC', False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True],
        ['Learning from new perspectives', False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True],
        ['Learn about different specialisms in deals', False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, ],
        ['Finding a mentor', False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False],
        ['Find a mentee', False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        ['Learn about a new market', False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False],
        ['Share knowledge about my market', False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False],
        ['Sharing work experiences', False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False],
        ['Finding people working on interesting projects', False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False],
        ['Meeting people that could join my project', False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        ['Learning about networks/initiatives within the firm', False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False],
        ['Finding people to join my network/group', False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        ['Learning technical skills', False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False],
        ['Helping people to learn technical skills', False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        ['Boosting my wellbeing & mental health', False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False],
        ['Looking for a better fit on my skills and talent', False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True]]

    def get_user_choice(self):
        return input('Your choice: ')

    def add_profile_data(self, profile_data, data=None, account=False):
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
            try:
                if int(index) not in self.selected_options:
                    selected_option = int(index) - 1
                    profile_data.insert(selected_option, data[selected_option])
                    print(profile_data)
                    self.selected_options.append(int(index))
                else:
                    print(Fore.RED + 'Option [ {} ] has already been selected!'.format(index))
            except (ValueError, IndexError):
                print(Fore.RED + 'Invalid input!')
                return
            

    def show_data(self, item_list, title):
        print(Fore.BLUE + f'Select a {title} from the list below:')
        for i, item in enumerate(item_list):
            print(Fore.BLUE + '{}: {}'.format(i + 1, item))
        print('q: Continue!')
        print("=" * 50 + '\n')
        # self.add_profile_data(data=item_list, profile_data=data, account=account)

    # Get and save all profile attributes
    def get_account_data(self) -> None:
        while len(self.account_data) != len(self.account_info_list):
            self.show_data(item_list=self.account_info_list, title='account_data')
            self.add_profile_data(data=self.account_info_list, profile_data=self.account_data, account=True)
        else:
            self.selected_options = []
            print(Fore.GREEN + 'Profile data added!' + '\n')
            self.profile.set_up_account(self.account_data)
            
    
    # Get and save all goals for the profile
    def get_goals(self) -> None:
        while len(self.goals) < 3:
            self.show_data(item_list=self.goal_list, title='goal')
            self.add_profile_data(data=self.goal_list, profile_data=self.goals)
        else:    
            self.selected_options = []
            print(Fore.GREEN + 'Goals added!' + '\n')
            self.profile.set_goals(self.goals)
            

    # Get and save all interests for the profile
    def get_interests(self) -> None:
        while len(self.interests) < 5:
            self.show_data(item_list=self.interest_list, title='interest')
            self.add_profile_data(data=self.interest_list, profile_data=self.interests)
        else:
            self.selected_options = []
            print(Fore.GREEN + 'Interests added!' + '\n')
            self.profile.set_interests(self.interests)


    def show_matching_options(self) -> None:
        print(Fore.BLUE + 'Select a matching option:')
        print('1: Print profile details')
        print('2: Start single profile matching')
        print('3: Recalculate profile matching')
        print('4: print complete profile details')
        print('q: Exit')

    def begin_matching(self) -> None:
        matching = True
        # self.match = Match()
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
        index_list = []
        index_list_2 = []
        other_list = []
        other_list_2 = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] is True:
                    other_list.append(i)
                    index_list.append(j)
                    print(self.matrix[i][j])
        print(index_list)
        print(other_list)
        for index in index_list:
            try:
                item = self.goal_list[index]
                if item not in other_list_2:
                    other_list_2.append(item)
            except IndexError:
                pass
        print(other_list_2)
        print(len(other_list_2))
               
                    
        # self.get_account_data()
        # self.get_goals()
        # self.get_interests()
        # self.save_data(self.profile)
        # self.begin_matching()

cri = Criteria()
cri.menu()
