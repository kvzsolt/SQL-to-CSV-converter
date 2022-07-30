import connection


@connection.connection_handler
def testquery(cursor):
    query = """
        SELECT *
        FROM countries
        """
    cursor.execute(query)
    return cursor.fetchall()

