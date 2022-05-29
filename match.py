 # Matching algorithm for two profiles based on the profile similarity metric 
from utils.utility import Utility
from colorama import Fore


class Match(Utility):
    def __init__(self) -> None:
        super().__init__()
        self.percentage = 0.0
        self.match_list = []
        self.goal_weight = 0.5
        self.interest_weight = 0.17
        self.account_weight = 0.33
    
    def calculate_all_attribute_weight(self, list) -> float:
        """
        Total: Weight = 1.0 + 3.0 + 2.0 = 6.0 
        ---------------------------------------------------------------------
        Goals: Weight = 3.0 / 6.0 = 0.5         [number of matched goals]
        Interests: Weight = 1.0 / 6.0 = 0.17    [number of matched interests]
        Account: Weight = 2.0 / 6.0 = 0.33      [number of matched accounts]
        """
        all_attribute_count = []
        for match in list:
            total_weight = 0
            try:
                if match['matched_goals_count']:
                    total_weight += round((self.calculate_weight(attribute_count=match['matched_goals_count'], total_count=3) * self.goal_weight), 0)
                if match['matched_interests_count']:
                    total_weight += round((self.calculate_weight(attribute_count=match['matched_interests_count'], total_count=5) * self.interest_weight), 0)
                if match['matched_account_count']:
                    total_weight += round((self.calculate_weight(attribute_count=match['matched_account_count'], total_count=4) * self.account_weight), 0)
                match['total_weight'] =  total_weight
            except KeyError:
                continue
        for x in list:
            if x["profile_id"] == list[0]["profile_id"]:
                continue
            print(Fore.YELLOW + str(x) + '\n')
    
    
    def calculate_weight(self, attribute_count, total_count) -> float:
        return round((attribute_count / total_count) * 100, 0)
        
    def get_profile_data(self, profile_id) -> dict:
        for profile in self.data:
            if profile['profile_id'] == profile_id:
                return profile
        return {}


    def start_single_profile_match(self, profile) -> None:
        current_profile_goals = len(profile.__dict__['goals'].goals)
        current_profile_interests = len(profile.__dict__['interests'].interests)
        current_profile_account = len(profile.__dict__['account'].account)
        self.match_manager(title='goals', current_profile=profile.__dict__)
        self.match_manager(title='interests', current_profile=profile.__dict__)
        self.match_manager(title='account', current_profile=profile.__dict__)
        
        all_matches = self.get_match_list()
        print(Fore.GREEN + 'Active Profile [Goals: {}, Interests: {}]'.format(current_profile_goals,current_profile_interests))
        preferred_match_list = [x for x in all_matches if x['matched_goals_count'] >= current_profile_goals and x['matched_interests_count'] >= current_profile_interests and x['matched_account_count'] >= current_profile_account]
        print(("=" * 100) + '\n')
        for x in preferred_match_list:
            if x["profile_id"] == profile.__dict__["profile_id"]:
                continue
            else:
                print(Fore.CYAN + str(x))
        print(("=" * 100) + '\n')
        print(Fore.GREEN + 'Preferred matched profiles: {}'.format(len(preferred_match_list)))
    
    
    def get_matched_profiles_data(self) -> list:
       for data in [self.get_profile_data(x['profile_id']) for x in self.match_list]:
           print(data)
        
    def match_manager(self, title, current_profile) -> None:
        self.percentage = 0.0
        matched_profile = {}
        profile_title = None
        
        if title == 'goals':
            profile_title = current_profile[title]
        elif title == 'interests':
            profile_title = current_profile[title]
        elif title == 'account':
            if current_profile['account']:
                profile_title = current_profile[title]
            else:
                return
            # print(profile_title)
        
        for (index, profile) in enumerate(self.data):
            for key, value in profile.items():
                if key == title:
                    list = value
                    counter = 0
                    loop_list = self.get_list(title=title, list=list)
                    for list_item in loop_list:
                        inner_loop_list = self.get_inner_list(title=title, profile_t=profile_title)
                        if list_item in inner_loop_list:
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
                    if title == 'account':
                        for match in self.match_list:
                            if match['profile_id'] == profile['profile_id']:
                                match['matched_account_count'] = counter
                    self.match_list.append(matched_profile)
                    self.percentage = 0.0
                    counter = 0
                    matched_profile = {}
        if title == 'goals':
            print(Fore.GREEN + 'Completed matching goals.')
        if title == 'interests':
            print(Fore.GREEN + 'Completed matching interests.')
        if title == 'account':
            print(Fore.GREEN + 'Completed matching accounts.')
    
    
    def get_list(self, title, list) -> list:
        return list.goals if title == 'goals' else list.interests if title == 'interests' else list.account
    

    def get_inner_list(self, title, profile_t) -> list:
        return profile_t.goals if title == 'goals' else profile_t.interests if title == 'interests' else profile_t.account if title == 'account' else []
        
   
    def get_match_list(self) -> list:
        list = []
        for x in self.match_list:
             try:
                if x['matched_goals_count']:
                    list.append(x)
             except KeyError:
                pass
        return list


    def check_matches_for_all_profiles(self) -> None:
        counter = 0
        for profile in self.data:
            current_profile_goals = len(profile['goals'].goals)
            current_profile_interests = len(profile['interests'].interests)
            current_profile_account = len(profile['account'].account)
            self.match_manager(title='goals', current_profile=profile)
            self.match_manager(title='interests', current_profile=profile)
            self.match_manager(title='account', current_profile=profile)
            all_matches = self.get_match_list()
            print(Fore.GREEN + 'Active Profile [id: {}, Goals: {}, Interests: {}, Account: {}]'.format(profile['profile_id'], current_profile_goals, current_profile_interests, current_profile_account))
            preferred_match_list = [x for x in all_matches if x['matched_goals_count'] > 0 and x['matched_interests_count'] > 0 and x['matched_account_count'] > 0]
            print((Fore.CYAN + "=" * 100))
            self.calculate_all_attribute_weight(list=preferred_match_list)
            match_count = 0
            for x in preferred_match_list:
                if x["profile_id"] == profile['profile_id']:
                    pass
                else:
                    match_count += 1
                    print(Fore.CYAN + str(x) + '\n')
            print(("=" * 100))
            print(Fore.GREEN + 'Matched profiles: {}'.format(match_count))
            print(Fore.CYAN + ("=" * 100) + '\n')
            self.match_list = []
            counter += 1
        print(Fore.YELLOW + 'Completed matching profiles: {}'.format(counter))


match = Match()
match.check_matches_for_all_profiles()