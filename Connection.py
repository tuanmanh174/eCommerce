import pymysql.cursors

def getConnection():
    connection = pymysql.connect(
                user = 'root',
                password = '',
                db = 'bt1',
                charset = 'utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
            )
    return connection