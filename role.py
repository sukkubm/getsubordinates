from collections import defaultdict


class Role:
    def __init__(self, id, name, parent):
        self.Id = id
        self.Name = name
        self.Parent = parent

    @staticmethod
    def setRoles(roles):
        """
      Sets roles dictionary and parent to role dictionary
      It also sets buildDescendantsMap function to descendants_map dictionary
      @input: roles list with Id, Name and Parent
      @return: descendants_map dictionary
      """
        parent_role_map = defaultdict(list)
        for role in roles:
            role_id = role["Id"]
            parent_id = role["Parent"]
            parent_role_map[parent_id].append(role_id)
        descendants_map = Role.buildDescendantsMap(parent_role_map)
        return descendants_map

    @staticmethod
    def buildDescendantsMap(parent_role_map):
        """
        Creates a dictionary with parent role as key and all its subordinate roles as value
        @input: parent_role_map dictionary with parent role as key and roles as value
        @return: descendants_map dictionary
        """
        descendants_map = defaultdict(list)
        for parent_role, child_roles in parent_role_map.items():
            descendants_map[parent_role].extend(child_roles)
            queue = child_roles.copy()
            while len(queue) != 0:
                first_element = queue.pop(0)
                c_role = parent_role_map.get(first_element)
                if not c_role:
                    continue
                descendants_map[parent_role].extend(c_role)
                queue.extend(c_role)
        return descendants_map
