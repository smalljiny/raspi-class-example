import pymysql.cursors
from encryption import password

def insert(email, pwd, connection):
    with connection.cursor() as cursor:
        sql = 'INSERT INTO `users` (`email`, `password`) VALUES (%s, %s);'
        cursor.execute(sql, (email, password.get(pwd)))

def get_password(email, connection):
    with connection.cursor() as cursor:
        sql = 'SELECT `id`, `password` FROM users WHERE email = %s;'
        cursor.execute(sql,(email,))
        rs = cursor.fetchone()

    if rs:
        return rs
    else:
        return None

def get_users(connection):
    with connection.cursor() as cursor:
        sql = 'SELECT `email` FROM users;'
        cursor.execute(sql)
        rs = cursor.fetchall()

    result = [];
    for row in rs:
        result.append({'email':row[0]})

    return result
