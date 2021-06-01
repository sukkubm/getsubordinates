from collections import defaultdict
from utils import throw_error


class User:
    def __init__(self, id, name, role):
        self.Id = id
        self.Name = name
        self.Role = role

    def getUser(self):
        # Returns id, name and role for a given user
        return {"Id": self.Id, "Name": self.Name, "Role": self.Role}

    @staticmethod
    def setUsers(users):
        """
        Sets users dictionary and role to user dictionary
        @input: users list with Id, Name and Role
        @return: users_map and role_user_map dictionary
        """
        users_map = {}
        role_user_map = defaultdict(list)
        for user in users:
            user_id = user["Id"]
            role_id = user["Role"]
            users_map[user_id] = User(user["Id"], user["Name"], role_id)
            role_user_map[role_id].append(User(user["Id"], user["Name"], role_id))
        return users_map, role_user_map

    @staticmethod
    def getSubOrdinates(user_id, users_map, role_user_map, descendants_map):
        """
        Get subordinates of a particular user using the role and fetching descendants_map 
        to get all subordinates and iterate through each to get the final result
        @input: user_id, users_map, role_user_map, descendants_map
        @return: result_list - Final result list with user details
        """
        result_list = []
        user = users_map.get(user_id)
        if not user:
            throw_error("User ID not found!")
        role_id = user.Role
        subordinate_ids = descendants_map.get(role_id)
        if not subordinate_ids:
            throw_error("No subordinates found!")
        for subordinate_id in subordinate_ids:
            users = role_user_map.get(subordinate_id)
            for user in users:
                result_list.append(user.getUser())
        return result_list
