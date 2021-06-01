import unittest

from user import User
from role import Role


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.users = [
            {"Id": 1, "Name": "Adam Admin", "Role": 1},
            {"Id": 2, "Name": "Emily Employee", "Role": 4},
            {"Id": 3, "Name": "Sam Supervisor", "Role": 3},
            {"Id": 4, "Name": "Mary Manager", "Role": 2},
            {"Id": 5, "Name": "Steve Trainer", "Role": 5},
        ]

        self.roles = [
            {"Id": 2, "Name": "Location Manager", "Parent": 1},
            {"Id": 3, "Name": "Supervisor", "Parent": 2},
            {"Id": 4, "Name": "Employee", "Parent": 3},
            {"Id": 5, "Name": "Trainer", "Parent": 3},
            {"Id": 1, "Name": "System Administrator", "Parent": 0},
        ]

    def test_set_users(self):
        users_map, role_user_map = User.setUsers(self.users)
        self.assertEqual(len(users_map), 5)
        first_user = users_map.get(1)
        self.assertIsNotNone(first_user)
        self.assertEqual("Adam Admin", first_user.Name)
        self.assertEqual(1, first_user.Id)
        self.assertEqual(1, first_user.Role)
        self.assertEqual(len(role_user_map), 5)
        first_role_user = role_user_map.get(1)
        self.assertEqual(len(first_role_user), 1)
        self.assertEqual("Adam Admin", first_role_user[0].Name)
        self.assertEqual(1, first_role_user[0].Id)
        self.assertEqual(1, first_role_user[0].Role)

    def test_set_roles_empty(self):
        users_map, role_user_map = User.setUsers([])
        self.assertEqual(len(users_map), 0)
        self.assertEqual(len(role_user_map), 0)

    def test_get_subordinates(self):
        descendants_map = Role.setRoles(self.roles)
        users_map, role_user_map = User.setUsers(self.users)
        result_list = User.getSubOrdinates(3, users_map, role_user_map, descendants_map)
        self.assertEqual(len(result_list), 2)
        self.assertEqual("Emily Employee", result_list[0]["Name"])
        self.assertEqual(2, result_list[0]["Id"])
        self.assertEqual(4, result_list[0]["Role"])
        self.assertEqual("Steve Trainer", result_list[1]["Name"])
        self.assertEqual(5, result_list[1]["Id"])
        self.assertEqual(5, result_list[1]["Role"])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
