import Member


class MemberDatabase:
    def __init__(self):
        self.database = []

    def is_present(self, member_id):
        for i in self.database:
            if i.get_id() == member_id:
                return True
            else:
                return False

    def add(self, member):
        if not self.is_present(member.get_id):
            self.database.append(member)
            return True
        else:
            return False

    def update(self, member):
        for i in self.database:
            if i.get_id() == member.get_id():
                self.database.remove(i)
                self.database.append(member)
                return True
        return False

    def retrieve(self, member_id):
        if (len(self.database) == 0):
            print("Nothing is in the database")
            return None
        for i in self.database:
            if i.get_id() == member_id:
                return i

        print("The member with the ID:", member_id, " is not in the database.")
        return None

    def delete(self, member_id):
        for i in self.database:
            if i.get_id() == member_id:
                self.database.remove(i)
                return True

        return False

    def login(self, member_id, password) -> Member:
        member = self.retrieve(member_id)
        if member.get_password() == password:
            return member
        else:
            return None
