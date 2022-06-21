import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host = 'yh-db.chyowr2bx2g2.ap-northeast-2.rds.amazonaws.com',
        database = 'practice',
        user = 'memo_user',
        password = 'memo1234'
    )
    return connection