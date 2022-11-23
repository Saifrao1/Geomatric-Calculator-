import datetime as dt


# u_name = input("Enter your  username: ")
# f_name = input("Enter your full name: ")


class Member:
    free_days = 365

    def __init__(self, uname, fname):
        self.username = uname
        self.fullname = fname
        self.is_active = True
        self.joind_date = dt.date.today()
        self.free_expires = dt.date.today() + dt.timedelta(days=Member.free_days)

    def joind_date(self) -> None:
        d = f"{self.fullname} is joind {self.joind_date: %d / %m / %Y}"
        return d

    # @classmethod
    # def setfreedays(cls, days):
    #     cls.free_days = days

    @staticmethod
    def currenttime():
        t = dt.datetime.now()
        return t

# how to create subclass


class Admin(Member):
    expiry_days = 365 * 100

    def __init__(self, uname, fname, secret_code):
        super().__init__(uname, fname)
        self.secret_code = secret_code


class User(Member):
    pass


Member.free_days = 90
new_guy = Member("Joe", "Joe Anderson")

s = Admin("SAIF", "SAIF UR REHMAN", "7294")

toe = User("Annie", "Jolia")

output = f"""
Current time  = {new_guy.currenttime(): %I:%M %p}
Date Joind  = {new_guy.joind_date: %d / %m /%Y}
Free Trial Experies  = {new_guy.free_expires: %d / %m /%Y}

Admin info  ={s.fullname} and expire date is {s.expiry_days} Code {s.secret_code}
new_user = '{toe.username}' and  joind {toe.joind_date: %d/%m/%Y} 



"""
print(output)
