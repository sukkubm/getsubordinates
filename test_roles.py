import unittest

from role import Role


class RolesTestCase(unittest.TestCase):
    def setUp(self):
        self.roles = [
            {"Id": 2, "Name": "Location Manager", "Parent": 1},
            {"Id": 3, "Name": "Supervisor", "Parent": 2},
            {"Id": 4, "Name": "Employee", "Parent": 3},
            {"Id": 5, "Name": "Trainer", "Parent": 3},
            {"Id": 1, "Name": "System Administrator", "Parent": 0},
        ]

    def test_set_roles(self):
        descendants_map = Role.setRoles(self.roles)
        self.assertEqual(len(descendants_map), 4)
        self.assertEqual(len(descendants_map.get(0)), 5)
        self.assertEqual(descendants_map.get(0), [1, 2, 3, 4, 5])

    def test_set_roles_empty(self):
        descendants_map = Role.setRoles([])
        self.assertEqual(len(descendants_map), 0)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
