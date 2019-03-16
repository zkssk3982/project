from member.database import Database


class MemberService:
    def __init__(self):
        pass

    @staticmethod
    def login(userid, password):
        print("서비스 어이디 {}, 비번 {}".format(userid, password))
        db = Database()
        row = db.login(userid, password)
        return row


