import pymysql.cursors

def get_measurements(room_id, start, end, connection):
    with connection.cursor() as cursor:
        sql = '''
            SELECT
            `M`.`datetime` AS `datetime`,
            `M`.`temperature` AS `temperature`,
            `M`.`humidity` AS `humidity`
            FROM `measurements` AS `M`
            WHERE `M`.`room` = %s AND `M`.`datetime` >= %s AND `M`.`datetime` <= %s;
        '''
        cursor.execute(sql, (room_id, start, end))
        rs = cursor.fetchall()

    data = [];
    for row in rs:
        data.append({
            'datetime':row[0],
            'temperature':row[1],
            'humidity':row[2]
        })

    return {
        'room':room_id,
        'start':start,
        'end':end,
        'data': data,
    }

def insert(params, connection):
    with connection.cursor() as cursor:
        sql = '''
            INSERT INTO `measurements`
            (`room`, `datetime`, `temperature`, `humidity`)
            VALUES (%s, %s, %s, %s);
        '''
        cursor.execute(sql, params)
        room_id = cursor.lastrowid

    return room_id
