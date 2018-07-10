# -*- coding:utf-8 -*-
from account.mysqldb import Dbcon


class User:
    """
    用户操作，包括获取用户ID，角色信息
    """
    def __init__(self):
        """
        :param:
        """
        self.Con = Dbcon().dbCon1()
        self.Cur = self.Con.cursor()

    def getPList(self, uid=''):
        """
        根据用户ID获取该用户下英雄列表
        :param uid: 用户ID
        :return: list 个人所拥有的人物
        """
        L1 = []
        uid = uid
        self.Cur.execute("select pname from p_user LEFT JOIN user_p_list on p_user.id = user_p_list.pid where user_p_list.uid={}".format(uid))
        if self.Cur:
            for p in self.Cur:
                L1.append(p[0])
        return L1

    def _closedb(self):
        self.Cur.close()
        self.Con.close()


if __name__ == '__main__':
    M = User()
    M.getPList(1)
