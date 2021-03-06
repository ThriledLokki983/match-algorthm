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
        Goals: Weight = 3.0 / 6.0 = 0.50         [number of matched goals]
        Interests: Weight = 1.0 / 6.0 = 0.17    [number of matched interests]
        Account: Weight = 2.0 / 6.0 = 0.33      [number of matched accounts]
        """
        for match in list[:]:
            total_weight = 0
            try:
                if match['matched_goals']:
                    matched_weight = round((self.calculate_weight(attribute_count=len(match['matched_goals']), total_count=3) * self.goal_weight), 0)
                    self.check_goal_compatibility(current_profile=match)
                    
                    total_weight += (matched_weight + 0)
                if match['matched_interests']:
                    total_weight += round((self.calculate_weight(attribute_count=len(match['matched_interests']), total_count=5) * self.interest_weight), 0)
                if match['matched_account']:
                    total_weight += round((self.calculate_weight(attribute_count=len(match['matched_account']), total_count=4) * self.account_weight), 0)
                match['total_weight'] =  total_weight
            except KeyError:
                continue
    
    def calculate_weight(self, attribute_count, total_count) -> float:
        return round((attribute_count / total_count) * 100, 0)
    
    
    def check_goal_compatibility(self, current_profile) -> None:
        profile_data = self.get_profile_data(current_profile['profile_id'])
        for profile in self.data:
            for goal in profile['goals'].goals:
                if self.check_goal_compatibility_part_of_goal(goal=goal, profile=profile_data) is True:
                    pass
                else:
                    self.calculate_compatibility(current_profile=current_profile)
              
                    
    def calculate_compatibility(self, current_profile) -> None:
        """
        Calculate compatibility of current profile with other profiles
        """
        all_list = []
        if len(current_profile['unmatched_goals'][0]['profile_to_compare_unmatched_items']) == 0:
            return
        else:
            for data in current_profile['unmatched_goals']:
                print("-" * 50)
                for x in [*data]:
                    all_list.append(data[x])
        if len(all_list) == 0:
            return
        else:
          common = [goal_item for goals in all_list for goal_item in goals] 
        print(common)
          

        
        
    def check_goal_compatibility_part_of_goal(self, goal, profile) -> bool:
        for profile_goal in profile['goals'].goals:
            if goal in profile_goal:
                return True
        return False
    
                    # profile['matched_goals'].remove(goal)
                    # current_profile['matched_goals'].remove(goal)
            #     print(goal)
        #         if goal in profile.goals:
        #             profile.matched_goals_count += 1
        #             self.match_list.append(profile.__dict__)
        # for goal in profile['goals'].goals:
            
        # Goals can be a total of '3' (Weight == 3 == 50%)
        # total number of goals can be three or less
        
        # profile('a', 'b')
        # profile_2('b', 'c', 'd') -- match of 1 goal
        
        # profile('a', 'b')
        # profile_2('b', 'c', 'd') -- compatible of 1 goal
        
        # 75%
        
        pass
        # TODO: get the list of goals for profile and perform a check on other profiles;
        # If current_profile is looking for someone to coach for example - then it is compatible with any profile that is looking for a coach (Ques: what then is the weight given to a scenario like this)
        # Have a category of list of goals and if an item from this category is for any two profiles we can say they are compatible
        # Matched == 1
        # Unmatched
        # Compatible == 2
    
    
    def calculate_interest_weight() -> float:
        pass
         # For interest -- each should have its own weight 1 - 2 - 3 ==> 1, 3 , 10
    #    (1/10) * 0.17 === 0.017

    def start_single_profile_match(self, profile) -> None:
        current_profile_id = profile['profile_id']
        current_profile_goals = len(profile.__dict__['goals'].goals)
        current_profile_interests = len(profile.__dict__['interests'].interests)
        current_profile_account = len(profile.__dict__['account'].account)
        self.match_manager(title='goals', current_profile=profile.__dict__)
        self.match_manager(title='interests', current_profile=profile.__dict__)
        self.match_manager(title='account', current_profile=profile.__dict__)
        
        all_matches = self.get_match_list()
        print(Fore.GREEN + f'Active Profile [id: {current_profile_id}, Goals: {current_profile_goals}, Interests: {current_profile_interests}, Account: {current_profile_account}]')
        preferred_match_list = [x for x in all_matches if x['matched_goals_count'] >= current_profile_goals or x['matched_interests_count'] >= current_profile_interests or x['matched_account_count'] >= current_profile_account]
        self.calculate_all_attribute_weight(list=preferred_match_list)
        self.print_top_6_matches(list=preferred_match_list, profile=profile)
        print(("=" * 100) + '\n')
        self.calculate_all_attribute_weight(list=preferred_match_list)
        # sorted_weight = sorted(preferred_match_list, key=lambda k: k['total_weight'], reverse=True)
        # print(sorted_weight)
        for x in preferred_match_list:
            if x["profile_id"] == profile.__dict__["profile_id"]:
                pass
            else:
                print(Fore.CYAN + str(x))
        print(("=" * 100) + '\n')
        print(Fore.GREEN + 'Total matched profiles: {}'.format(len(preferred_match_list)))

        
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
        for (index, profile) in enumerate(self.data):
            for key, value in profile.items():
                if key == title:
                    list = value
                    counter_matched = 0
                    list_matched = [{'current_profile_matched_items': []}]
                    list_unmatched = [{'profile_to_compare_unmatched_items': [], 'current_profile_unmatched_items': []}]
                    counter_unmatched = 0
                    loop_list = self.get_list(title=title, list=list)
                    for list_item in loop_list:
                        inner_loop_list = self.get_inner_list(title=title, profile_t=profile_title)
                        if list_item in inner_loop_list:
                            counter_matched += 1
                            list_matched[0]['current_profile_matched_items'].append(list_item)
                        else:
                            counter_unmatched += 1
                            list_unmatched[0]['current_profile_unmatched_items'].append(list_item)
                            for item in inner_loop_list:
                                if item in (list_matched[0]['current_profile_matched_items']) or item in list_unmatched[0]['profile_to_compare_unmatched_items']:
                                    pass
                                else:
                                    list_unmatched[0]['profile_to_compare_unmatched_items'].append(item)
                    # if title == 'goals':
                        # print(Fore.WHITE + ("=" * 100))
                        # print(Fore.BLUE + 'LOOP LIST')
                        # print(Fore.LIGHTCYAN_EX + str(loop_list))
                        # print(Fore.BLUE + 'INNER LOOP LIST')
                        # print(Fore.LIGHTCYAN_EX + str(inner_loop_list))
                        # print(Fore.GREEN + 'MATCHED LIST')
                        # print(Fore.GREEN + str(list_matched))
                        # print(Fore.RED + 'UNMATCHED LIST')
                        # print(Fore.RED + str(list_unmatched))
                        # print(Fore.WHITE + ("=" * 100))
                    matched_profile["profile_id"] = profile['profile_id']
                    if title == 'goals':
                        # matched_profile["matched_goals_count"] = counter_matched
                        matched_profile['matched_goals'] = list_matched
                        matched_profile['unmatched_goals'] = list_unmatched
                        # matched_profile["goals_unmatched"] = counter_unmatched
                    if title == 'interests':
                        for match in self.match_list:
                            if match['profile_id'] == profile['profile_id']:
                                # match['matched_interests_count'] = counter_matched
                                # match['unmatched_interests_count'] = counter_unmatched
                                match['matched_interests'] = list_matched
                                match['unmatched_interests'] = list_unmatched
                    if title == 'account':
                        for match in self.match_list:
                            if match['profile_id'] == profile['profile_id']:
                                # match['matched_account_count'] = counter_matched
                                # match['unmatched_account_count'] = counter_unmatched
                                match['matched_account'] = list_matched
                                match['unmatched_account'] = list_unmatched
                    self.match_list.append(matched_profile)
                    self.percentage = 0.0
                    counter_matched = 0
                    counter_unmatched = 0
                    matched_profile = {}
        self.complete(title)
       
    

    def check_matches_for_all_profiles(self) -> None:
        counter = 0
        for profile in self.data:
            current_profile_id = profile['profile_id']
            current_profile_goals = len(profile['goals'].goals)
            current_profile_interests = len(profile['interests'].interests)
            current_profile_account = len(profile['account'].account)
            self.match_manager(title='goals', current_profile=profile)
            self.match_manager(title='interests', current_profile=profile)
            self.match_manager(title='account', current_profile=profile)
            all_matches = self.get_match_list()
            print(Fore.GREEN + f'Active Profile [id: {current_profile_id}, Goals: {current_profile_goals}, Interests: {current_profile_interests}, Account: {current_profile_account}]')
            preferred_match_list = [y for (x, y) in enumerate(all_matches) if len(y['matched_goals']) > 0 or len(y['matched_interests']) > 0 or len(y['matched_account']) > 0]
            print((Fore.CYAN + "=" * 100))
            self.calculate_all_attribute_weight(list=preferred_match_list)
            match_count = 0
            self.print_top_6_matches(list=preferred_match_list, profile=profile)
            for x in preferred_match_list:
                if x["profile_id"] == profile['profile_id']:
                    pass
                else:
                    match_count += 1
                    # print(Fore.CYAN + str(x) + '\n')
            print(("=" * 100))
            print(Fore.GREEN + 'Matched profiles: {}'.format(match_count))
            print(Fore.CYAN + ("=" * 100) + '\n')
            self.match_list = []
            counter += 1
        print(Fore.YELLOW + 'Completed matching profiles: {}'.format(counter))
    
    
    def print_top_6_matches(self, list, profile) -> None:
        sorted_weight = sorted(list, key=lambda k: k['total_weight'], reverse=True)
        for x in sorted_weight[:7]:
            if x['profile_id'] == profile['profile_id']:
                pass
            else:
                # print(Fore.CYAN + str(x) + '\n')
                pass

    
    def get_profile_data(self, profile_id) -> dict:
        for profile in self.data:
            if profile['profile_id'] == profile_id:
                return profile
        return {}
    
    
    def get_match_list(self) -> list:
        list = []
        for x in self.match_list:
             try:
                if x['matched_goals']:
                    list.append(x)
             except KeyError:
                pass
        return list  
        
        
    def get_matched_profiles_data(self) -> list:
       for data in [self.get_profile_data(x['profile_id']) for x in self.match_list]:
           print(data)
     
     
    def get_inner_list(self, title, profile_t) -> list:
        return profile_t.goals if title == 'goals' else profile_t.interests if title == 'interests' else profile_t.account if title == 'account' else []      
    
    
    def get_list(self, title, list) -> list:
        return list.goals if title == 'goals' else list.interests if title == 'interests' else list.account if title == 'account' else []
     
    def complete(self, title):
        if title == 'goals':
            print(Fore.GREEN + 'Completed matching goals.')
        if title == 'interests':
            print(Fore.GREEN + 'Completed matching interests.')
        if title == 'account':
            print(Fore.GREEN + 'Completed matching accounts.')
           
# match = Match()
# match.check_matches_for_all_profiles()