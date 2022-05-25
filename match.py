 # Matching algorithm for two profiles based on the profile similarity metric 
from utils.utility import Utility


class Match(Utility):
    def __init__(self, profile_one) -> None:
        super().__init__()
        # print( self.data)
        self.profile_one = profile_one
        self.percentage = 0.0
        self.match_list = []
        
    def start_match(self) -> None:
         profile_goals = self.profile_one.__dict__['goals']
         for (index, block) in enumerate(self.data):
            for key, value in block.items():
                if key == 'goals':
                    goals = value
                    for goal in goals.goals:
                        if goal in profile_goals.goals:
                            # self.percentage += 1
                            self.match_list.append(block['profile_id'])
                    self.percentage = 0.0
                elif key == 'interests':
                    interests = value
            # check in the profile list for the goals of the profile that has the same goals
         print( self.match_list)
            
    def check_match(self) -> None:
        pass
