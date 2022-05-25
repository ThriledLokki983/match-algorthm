import string
import random
from utils.goal import Goal
from utils.interest import Interest


class Profile:
    def __init__(self) -> None:
        self.id = None
        self.goals = []
        self.interests = []
        
    def set_goals(self, goals) -> None:
        goals = Goal(profile=self.id, goals=goals)
        self.goals = goals.goals
    
    
    def generate_id(self) -> str:
        id = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(30))
        return id
    
    def create_profile(self) -> None:
        self.id = self.generate_id()
        return self.id
        
prof = Profile()
   

    
    
    