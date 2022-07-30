import mysql.connector
from mysql.connector import Error


def open_database():
    try:
        connection = mysql.connector.connect(host="localhost",
                                             user="kvzsolt",
                                             passwd="password",
                                             db="sqltocsv")
    except Error as e:
        print("Error while connection to MySQL", e)
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        dict_cur = connection.cursor(dictionary=True)
        ret_value = function(dict_cur, *args, **kwargs)
        dict_cur.close()
        connection.close()
        return ret_value

    return wrapper
