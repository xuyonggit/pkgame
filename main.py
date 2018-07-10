# -*- coding:utf-8 -*-
from account.login import Login
from UserInfo.user import User

class M1:
    def __init__(self):
        self.username, self.userid = Login().check()


    def meau(self):
        while True:
            oper = input("[{}]:".format(self.username))
            if oper in ['logout', 'exit']:
                print("退出登录")
                self.__init__()
            elif oper == 'ls':
                for pname in User().getPList(self.userid):
                    print(pname)


if __name__ == '__main__':
    M = M1()
    M.meau()
