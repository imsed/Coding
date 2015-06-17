__author__ = 'imsed'

def connect_to_mysql_database(db_ip, db_user, db_passwd, db_name):
    db_connection = None
    db_connection = MySQLdb.connect(db_ip, db_user, db_passwd, db_name)
    return db_connection


def dict_query_mysql_database(db_connection, query):
    rc = None
    with db_connection:
        db_cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)
        db_cursor.execute(query)
        rc = db_cursor.fetchall()
    db_cursor.close()
    return rc

