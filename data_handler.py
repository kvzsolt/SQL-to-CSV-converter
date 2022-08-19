import connection
import os


@connection.connection_handler
def get_database_name(cursor):
    query = """
        SHOW TABLES FROM {dbname}
        """.format(dbname=os.environ.get('MYSQL_DB_NAME')) #fixed
    cursor.execute(query)
    return cursor.fetchall()


@connection.connection_handler
def get_all_data(cursor, dbname):
    query = """
    SELECT * FROM {dbname}
    """.format(dbname=dbname)
    cursor.execute(query)
    return cursor.fetchall()
