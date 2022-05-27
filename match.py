 # Matching algorithm for two profiles based on the profile similarity metric 
from utils.utility import Utility
from colorama import Fore


class Match(Utility):
    def __init__(self, profile_one) -> None:
        super().__init__()
        # print( self.data)
        self.profile_one = profile_one
        self.percentage = 0.0
        self.match_list = []
        
    def start_match(self) -> None:
         self.match_manager(title='goals')
         self.match_manager(title='interests')
         print(self.match_list)

    
    def match_manager(self, title) -> None:
        self.percentage = 0.0
        matched_profile = {}
        profile_title = self.profile_one.__dict__[title]
        for (index, profile) in enumerate(self.data):
            for key, value in profile.items():
                if key == title:
                    list = value
                    counter = 0
                    for list_item in list.goals if title == 'goals' else list.interests:
                        if list_item in profile_title.goals if title == 'goals' else list_item in profile_title.interests:
                            counter += 1
                            if title == 'goals':
                                self.percentage += 0.33
                            if title == 'interests':
                                self.percentage += 0.20
                    matched_profile["profile_id"] = profile['profile_id']
                    if title == 'goals':
                        matched_profile["matched_goals_count"] = counter
                    if title == 'interests':
                        for match in self.match_list:
                            if match['profile_id'] == profile['profile_id']:
                                match['matched_interests_count'] = counter
                    
                    self.match_list.append(matched_profile)
                    self.percentage = 0.0
                    counter = 0
                    matched_profile = {}
        print('Done!')
   

    def interest_match(self) -> None:
        pass
            
    def check_match(self) -> None:
        pass
