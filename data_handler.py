import connection


@connection.connection_handler
def get_database_name(cursor):
    query = """
        SHOW TABLES FROM sqltocsv
        """
    cursor.execute(query)
    return cursor.fetchall()


@connection.connection_handler
def get_all_data(cursor, dbname):
    query = """
    SELECT * FROM {dbname}
    """.format(dbname=dbname)
    cursor.execute(query)
    return cursor.fetchall()
