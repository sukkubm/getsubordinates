import sys

from role import Role
from user import User
from utils import throw_error

roles = [
    {"Id": 1, "Name": "System Administrator", "Parent": 0},
    {"Id": 2, "Name": "Location Manager", "Parent": 1},
    {"Id": 3, "Name": "Supervisor", "Parent": 2},
    {"Id": 4, "Name": "Employee", "Parent": 3},
    {"Id": 5, "Name": "Trainer", "Parent": 3},
]


users = [
    {"Id": 1, "Name": "Adam Admin", "Role": 1},
    {"Id": 2, "Name": "Emily Employee", "Role": 4},
    {"Id": 3, "Name": "Sam Supervisor", "Role": 3},
    {"Id": 4, "Name": "Mary Manager", "Role": 2},
    {"Id": 5, "Name": "Steve Trainer", "Role": 5},
]


if __name__ == "__main__":
  try:
    user_input = sys.argv[1]
    if not user_input.isnumeric():
        throw_error("User input must be a number")
  except IndexError:
      throw_error("User input is mandatory!")

  descendants_map = Role.setRoles(roles)

  users_map, role_user_map = User.setUsers(users)

  result = User.getSubOrdinates(
      int(user_input), users_map, role_user_map, descendants_map
  )
  print(result)

