
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

        # example list of members
        self._members = [ {"id": self._generateId(), "first_name": "John", "last_name": "Jackson", "age": "33 Years old", "Lucky Numbers": [7, 13, 22]}, {"id": self._generateId(), "first_name": "Jane", "last_name": "Jackson", "age": "35 Years old", "Lucky Numbers": [10, 14, 3]}, {"id": self._generateId(), "first_name": "Jimmy", "last_name": "Jackson", "age": "5 Years old", "Lucky Numbers": [1]} ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if member["id"] is None:
            member["id"]= self._generateId()
        if member:
            self._members.append(member)
            return True
        else:
            return False

    def delete_member(self, id):
        for i, member in enumerate(self._members, start=0):
            if member["id"] == int(id):
                self._members.pop(i)
                return {"done": True}
        return None

    def get_member(self, id):
        for member in self._members:
            if member["id"] == int(id):
                return member
        return {"id": "", "first_name": "", "age": "", "lucky_numbers": [] }
        
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
