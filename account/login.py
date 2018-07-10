# -*- coding:utf-8 -*-
from account import mysqldb


class Login:
    def __init__(self):
        """
        认证系统
        """
        self.Con = mysqldb.Dbcon().dbCon1()
        self.Cur = self.Con.cursor()

    def check(self):
        check_u = 0
        check_p = 0
        while check_u == 0:
            username = input("请输入用户名 : ")
            try:
                self.Cur.execute("select id,upasswd from user where uname='{}'".format(username))
                if self.Cur:
                    for u in self.Cur:
                        check_u = 1
                        while check_p == 0:
                            passwd = input("请输入用户[{}]的密码 : ".format(username))
                            if passwd == u[1]:
                                print("登录成功")
                                check_p = 1
                                return username, u[0]
                                _CloasDb
                            else:
                                print("用户密码错误")
                    else:
                        print("用户名不存在,请重新输入")
            except:
                self._CloasDb()

    def _CloasDb(self):
        self.Cur.close()
        self.Con.close()


if __name__ == '__main__':
    Main = Login()
    print(Main.check())
