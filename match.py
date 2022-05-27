 # Matching algorithm for two profiles based on the profile similarity metric 
from utils.utility import Utility
from colorama import Fore


class Match(Utility):
    def __init__(self) -> None:
        super().__init__()
        self.percentage = 0.0
        self.match_list = []
        
    def start_single_profile_match(self, profile) -> None:
        # print(profile.__dict__)
        current_profile_goals = len(profile.__dict__['goals'].goals)
        current_profile_interests = len(profile.__dict__['interests'].interests)
        self.match_manager(title='goals', current_profile=profile.__dict__)
        self.match_manager(title='interests', current_profile=profile.__dict__)
        all_matches = self.get_match_list()
        print(Fore.GREEN + 'Active Profile [Goals: {}, Interests: {}]'.format(current_profile_goals,current_profile_interests))
        preferred_match_list = [x for x in all_matches if x['matched_goals_count'] >= current_profile_goals and x['matched_interests_count'] >= current_profile_interests]
        print(("=" * 100) + '\n')
        for x in preferred_match_list:
            print(Fore.CYAN + str(x))
        print(("=" * 100) + '\n')
        print(Fore.GREEN + 'Preferred matched profiles: {}'.format(len(preferred_match_list)))

    
    def match_manager(self, title, current_profile) -> None:
        self.percentage = 0.0
        matched_profile = {}
        profile_title = current_profile[title]
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
        if title == 'goals':
            print(Fore.GREEN + 'Completed matching goals.')
        if title == 'interests':
            print(Fore.GREEN + 'Completed matching interests.')
   
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
            self.match_manager(title='goals', current_profile=profile)
            self.match_manager(title='interests', current_profile=profile)
            all_matches = self.get_match_list()
            print(Fore.GREEN + 'Active Profile [Goals: {}, Interests: {}]'.format(current_profile_goals, current_profile_interests))
            preferred_match_list = [x for x in all_matches if x['matched_goals_count'] >= current_profile_goals and x['matched_interests_count'] >= current_profile_interests]
            print((Fore.CYAN + "=" * 100))
            for x in preferred_match_list:
                print(Fore.CYAN + str(x))
            print(("=" * 100))
            print(Fore.GREEN + 'Matched profiles: {}'.format(len(preferred_match_list)))
            print(Fore.CYAN + ("=" * 100) + '\n')
            self.match_list = []
            counter += 1
        print(Fore.YELLOW + 'Completed matching profiles: {}'.format(counter))
