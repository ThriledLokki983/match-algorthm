import string
import random
from utils.goal import Goal
from utils.interest import Interest
from collections import OrderedDict


class Profile:
    def __init__(self) -> None:
        self.profile_id = None
        self.goals = []
        self.interests = []

    def set_goals(self, goals) -> None:
        goals = Goal(goals=goals)
        self.goals = goals
        # self.goals = goals.goals

    def to_ordered_dict(self):
        return OrderedDict([('profile', self.profile_id), ('goals', self.goals), ('interests', self.interests)])

    def set_interests(self, interests) -> None:
        interests = Interest(interests=interests)
        self.interests = interests

    def generate_id(self) -> str:
        id = ''.join(random.choice(string.ascii_lowercase + string.digits)
                     for _ in range(30))
        return id

    def create_profile(self) -> None:
        self.profile_id = self.generate_id()
        return self.profile_id


prof = Profile()
