from utils.goal import Goal
from utils.interest import Interest
from pickle import dump, load

class Criteria: 
    def __init__(self, profile) -> None:
        self.profile = None
        self.goals = []
        self.interests = []
        self.profile = profile
        
    def get_user_choice(self):
        return input('Your choice: ')
    
    def show_goals(self):
        print('Select a goal from the list below:')
        print('1: Getting to know new communities in PwC')
        print('2: Working more x-LoS with PwC')
        print('3: Fostering an inclusive working environment')
        print('q: Continue!')
    
    def show_interests(self):
        print('Select an interest from the list below:')
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
                show_available_goals = False
        else: 
            print('Goals added!')
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
                show_available_interest = False
        else:
            print('Interests added!')
        print('Done!')
            
    def save_data(self) -> None:
        """
        Get the user's interests and goals and save them to a file for the currently active profile.
        """
        try:
            if self.profile != None:
                with open('goals-interests-profiles.pickle', 'ab') as file:
                    saveable_chain = []
                    saveable_chain.append(self.profile)
                    if len(self.goals) > 0:
                        saveable_chain.append(Goal(goals=self.goals).__str__())
                    if len(self.interests) > 0:
                        saveable_chain.append(Interest(interests=self.interests).__str__())
                    # file.write(str(saveable_chain) + '\n')
                    dump(saveable_chain, file)
            else:
                print("No profile found")
        except IOError:
            print('Error: Could not save data to file.')
    
    
    def load_data(self) -> None:
        with open('goals-interests-profiles.pickle', 'r') as file:
            f_content = file.readlines()
            for line in f_content:
                print(line)
            
                
                
    
    def load_interests(self, profile) -> None:
        pass
    
    def get_user_choice(self):
        return input('Your choice: ')
    
    def menu(self):
        self.get_goals()
        self.get_interests()
        # print('Goals: ' + str(self.goals))
        # print('Interests: ' + str(self.interests))
        self.save_data()
        self.load_data()