from datetime import datetime
import mysql.connector

DATABASE_HOST = '157.88.58.134'
DATABASE_PORT = '5584'
DATABASE_USER = 'kave'
DATABASE_PASSWORD = 'hola'
DATABASE_NAME = 'cliente1'

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def get_all_temperatures(cnx, from_date: datetime, to_date: datetime) -> list:
    from_date_str = from_date.strftime(DATETIME_FORMAT)
    to_date_str = to_date.strftime(DATETIME_FORMAT)

    query = "SELECT dato " \
            "FROM mediciones M " \
            "WHERE M.time BETWEEN '{}' AND '{}'".format(
        from_date, to_date
    )

    cursor = cnx.cursor()
    cursor.execute(query)

    result_set = [r[0] for r in cursor]

    return result_set


def crear_conexiones():
    cnx = mysql.connector.connect(host=DATABASE_HOST, port=DATABASE_PORT,
                                  user=DATABASE_USER, password=DATABASE_PASSWORD)
    cnx.database = DATABASE_NAME
    return cnx
