import datetime as dt


class Member:
    age = 17

    def __init__(self, uname, fname, age):
        self.username = uname
        self.fullname = fname

    def join_date(self):
        d = dt.date.today()
        return d

    def member_age(self):
        if self.age < 17:
            print("NOT ALLOWED")
        else:
            print("Allowed")

    def ge_status(self):
        return


class Admin(Member):
    def __init__(self, uname, fname, age, secret_code):
        super().__init__(uname, fname, age)
        self.secret_code = secret_code


class User(Member):
    pass


ann = Member("Anna", "Annarao", 16)

rao = Admin("SAif", "RAO", "RAOSA", 17)

jo = User("jolie", "ford", 18)

print(jo.member_age())
