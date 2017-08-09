from __future__ import print_function
import serial
import sys
import pymysql.cursors
import pymysql
from time import localtime
from pymysql import MySQLError
from sensors.loggers.logger import create_log
from time import sleep
from re import match

logger = create_log()

# Global variables
DB_HOST = '157.88.58.134'
DB_PORT = 5584
DB_USER = 'kave'
DB_PASS = 'hola'
DB_NAME = 'cliente1'
ARD_SERIAL_PORT = '/dev/ttyACM0'  # serial port connection Arduino
ARD_BD = 9600


def main():
    cnx = connect_db()
    ser = connect_arduino()

    while True:
        line_list = read_arduino(ser, cnx)
        send_data_db(cnx, line_list)


def send_data_db(cnx: pymysql.connect, line_list: list):
    try:
        id = line_list[0]
        sensor_num = line_list[1]
        value = line_list[2]
        query = "INSERT INTO reading(id, sensor_num, value, time)" \
                "VALUES (%s, %s, %s, %s)"
        args = [id, sensor_num, value, localtime()]
        cursor = cnx.cursor()
        cursor.execute(query, args)
        cnx.commit()
        cursor.close()
    except MySQLError as err:
        logger.error(err)


def read_arduino(ser: serial.Serial(), cnx: pymysql.connect) -> list:
    line_list = []
    regex = r'[0-9]\s[0-9]\s[0-9][0-9]\.[0-9][0-9]'
    try:
        line = ser.readline()
        line_2 = line.decode('utf-8')
        if match(regex, line_2):
            line_list.append(int(line.split()[0]))
            line_list.append(int(line.split()[1]))
            line_list.append(float(line.split()[2]))
        else:
            if line == '':
                ser.close()
                sleep(2)
                ser.open()
                logger.info('Reset ser')
            else:
                logger.info('Bad line from Arduino: {}'.format(line))
                ser.close()
                sleep(2)
                ser.open()
                logger.info('Reset ser from bad line Arduino')
    except Exception as err:
        logger.error(err)
    return line_list


def connect_db() -> pymysql.connect:
    try:
        cnx = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER,
                              password=DB_PASS, db=DB_NAME)
        logger.info('Connect to DB: ' + DB_NAME)
    except MySQLError as err:
        logger.error(err)
    return cnx


# TODO comprobar puerto y en caso de erro probar siguientes Arduino
def connect_arduino() -> serial.Serial():
    ser = ''
    try:
        ser = serial.Serial(ARD_SERIAL_PORT, ARD_BD)
        logger.info('Connecto to arduino port: ' + ARD_SERIAL_PORT)
    except Exception:
        err = sys.exc_info()[0]
        logger.error(err)
    return ser


if __name__ == '__main__':
    main()
