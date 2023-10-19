"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # Example list of members
        self._members = [{'id': 1,
                          'first_name': 'John',
                          'last_name': 'Jackson',
                          'age': 33,
                          'lucky_numbers': [7, 13, 22]},
                         {'id': self._generateId(),
                          'first_name': 'Jane',
                          'last_name': 'Jackson',
                          'age': 35,
                          'lucky_numbers': [10, 14, 3]},
                         {'id': self._generateId(),
                          'first_name': 'Jimmy',
                          'last_name': 'Jackson',
                          'age': 5,
                          'lucky_numbers': [1]}]
    
    # Read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Fill this method and update the return
        member["last_name"] = self.last_name
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        # Fill this method and update the return
        pass

    def get_member(self, id):
        # Opción 1: list comprehension
        result = [member for member in self._members if member["id"] == id]
        # Opción 2: Standard
        # result = []
        # for member in self._members:
        #    if member["id"] == id:
        #        result.append(member)
        # Opción 3: lambda function
        # result = list(filter(lambda member: member["id"] == id, self._members ))
        return result

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
