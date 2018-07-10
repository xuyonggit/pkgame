import pymysql


class Dbcon:
    """
    mysql 数据连接
    """
    def __init__(self):
        """
        :return: pymysql.connection
        """

    def dbCon1(self):
        return pymysql.connect(
            host='mysql.local.com',
            port=3306,
            user='pkgame',
            password='pkgame',
            database='pkgame',
            charset='utf8mb4'
        )
