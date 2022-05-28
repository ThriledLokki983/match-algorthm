import string
import random
from utils.goal import Goal
from utils.interest import Interest
from account import Account
from collections import OrderedDict


class Profile:
    def __init__(self) -> None:
        self.profile_id = None
        self.account = []
        self.goals = []
        self.interests = []

    def set_goals(self, data) -> None:
        goals = Goal(goals=data)
        self.goals = goals
    
    def set_interests(self, data) -> None:
        interests = Interest(interests=data)
        self.interests = interests
    
    def set_up_account(self, data):
        account = Account(account_data=data)
        # account.__dict__['account'].append(self.profile_id)
        self.account = account

    def to_ordered_dict(self):
        return OrderedDict([('profile', self.profile_id), ('goals', self.goals), ('interests', self.interests)])

    def generate_id(self) -> str:
        """
        Generates a random profile id
        :return:
        """
        id = ''.join(random.choice(string.ascii_lowercase + string.digits)
                     for _ in range(30))
        return id

    def create_profile(self) -> None:
        account = []
        self.profile_id = self.generate_id()
        account.append(self.profile_id)
        print(account)
        return self.profile_id


# prof = Profile()
