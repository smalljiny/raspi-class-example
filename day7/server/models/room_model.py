import pymysql.cursors
from encryption import access_key

def get_rooms(connection):
    with connection.cursor() as cursor:
        sql = 'SELECT `id`, `name`, `ip`, `boiler`, `humidifier`, `conneted` FROM `rooms`;'
        cursor.execute(sql)
        rs = cursor.fetchall()

    result = [];
    for row in rs:
        result.append({
            'id':row[0],
            'name':row[1],
            'ip':row[2],
            'boiler':row[3],
            'humidifier':row[4],
            'conneted':row[5]
        })

    return result

def create_room(params, connection):
    with connection.cursor() as cursor:
        sql = '''
            INSERT INTO `rooms`
            (`name`, `ip`, `max_temperature`, `min_temperature`, `max_humidity`, `min_humidity`, `key`)
            VALUES
            (%s, %s, %s, %s, %s, %s, 'None');
        '''
        cursor.execute(sql, params)
        room_id = cursor.lastrowid

    return room_id

def update_ip(id, ip, connection):
    key = access_key.get(ip, id)

    with connection.cursor() as cursor:
        sql = 'UPDATE `rooms` SET `ip` = %s, `key` = %s WHERE `id` = %s;'
        cursor.execute(sql, (ip, key, id))

def get_room(id, connection):
    with connection.cursor() as cursor:
        sql = '''
            SELECT `id`, `name`, `ip`, `key`, `max_temperature`, `min_temperature`,
            `max_humidity`, `min_humidity`, `boiler`, `humidifier`, `conneted`
            FROM `raspi`.`rooms` WHERE id = %s;
        '''
        cursor.execute(sql, id)
        row = cursor.fetchone()

    result = {
        'id': row[0],
        'name': row[1],
        'ip': row[2],
        'key': row[3],
        'max_temperature': row[4],
        'min_temperature': row[5],
        'max_humidity': row[6],
        'min_humidity': row[7],
        'boiler': row[8],
        'humidifier': row[9],
        'conneted': row[10]
    }

    return result
