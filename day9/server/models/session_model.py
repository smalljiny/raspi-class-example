import pymysql.cursors
from encryption import session_token

def insert(token, connection):
    decoded = session_token.decode(token)

    with connection.cursor() as cursor:
        sql = 'INSERT INTO `sessions` (`uid`, `token`, `expiration_date`) VALUES (%s, %s, %s);'
        cursor.execute(sql, (decoded['uid'], token, decoded['exp']))

def delete(token, connection):
    with connection.cursor() as cursor:
        sql = 'DELETE FROM `sessions` WHERE `token` = %s;'
        cursor.execute(sql, (token,))

def update(old_token, new_token, connection):
    decoded = session_token.decode(new_token)

    with connection.cursor() as cursor:
        sql = 'UPDATE `sessions` SET `token` = %s, `expiration_date` = %s WHERE `token` = %s;'
        cursor.execute(sql, (new_token, decoded['exp'], old_token))
