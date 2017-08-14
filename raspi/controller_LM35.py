from __future__ import print_function
import serial
import sys
import pymysql.cursors
import pymysql
from time import localtime
from pymysql import MySQLError
from modules.logger import create_log
from time import sleep
from re import match
import logging

logger = create_log()

# Global variables
DB_HOST = '157.88.58.134'
DB_PORT = 5584
DB_USER = 'kave'
DB_PASS = 'hola'
DB_NAME = 'cliente1'
ARD_SERIAL_PORT = '/dev/ttyACM0'  # serial port connection Arduino
ARD_BD = 9600
FLAG_RECONNECT = True

def main():
    while True:
        global FLAG_RECONNECT
        cnx = connect_db()
        ser = connect_arduino()

        while FLAG_RECONNECT == False:
            line_list = read_arduino(ser, cnx)
            send_data_db(cnx, line_list)
        # logger.info('Flag main before change: {}'.format(FLAG_RECONNECT))
        FLAG_RECONNECT = False
        # logger.info('Flag main after change: {}'.format(FLAG_RECONNECT))


def read_arduino(ser: serial.Serial(), cnx: pymysql.connect) -> list:
    global FLAG_RECONNECT
    line_list = [100, 1, 1]
    regex = r'[0-9]\s[0-9]\s[0-9][0-9]\.[0-9][0-9]'
    try:
        line = ser.readline()
        line_2 = line.decode('utf-8')
        if match(regex, line_2):
            # line_list.append(int(line.split()[0]))
            # line_list.append(int(line.split()[1]))
            # line_list.append(float(line.split()[2]))
            line_list[0] = (int(line.split()[0]))
            line_list[1] = (int(line.split()[1]))
            line_list[2] = (float(line.split()[2]))
        else:
            logger.info('Bad line from Arduino: {}'.format(line))
            ser.close()
            sleep(2)
            ser.open()
            logger.info('Reset Arduino connection')
    except Exception as err:
        logger.error(err)
        FLAG_RECONNECT = True
    return line_list


def send_data_db(cnx: pymysql.connect, line_list: list):
    global FLAG_RECONNECT
    if line_list[0] != 100:
        id = line_list[0]
        sensor_num = line_list[1]
        value = line_list[2]
        try:
            query = "INSERT INTO reading(id, sensor_num, value, time)" \
                    "VALUES (%s, %s, %s, %s)"
            args = [id, sensor_num, value, localtime()]
            cursor = cnx.cursor()
            cursor.execute(query, args)
            cnx.commit()
            cursor.close()
        except MySQLError as err:
            logger.error(err)
            cursor.close()
            cnx.close()
            FLAG_RECONNECT = True
            # logger.error(err.args[0])
            # logger.findCaller(stack_info=True)
            if err.args[0] == 2013:
                logger.info('Flag: {}'.format(FLAG_RECONNECT))
    else:
        logger.info('Bad data from Arduino: {}'.format(line_list))
        FLAG_RECONNECT = True


def connect_db() -> pymysql.connect:
    try:
        cnx = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER,
                              password=DB_PASS, db=DB_NAME)
        logger.info('Connect to DB: ' + DB_NAME)
    except MySQLError as err:
        logger.error(err)
        #logger.findCaller(stack_info=True)
    return cnx


# TODO: comprobar puerto y en caso de erro probar siguientes Arduino
def connect_arduino() -> serial.Serial():
    ser = ''
    try:
        ser = serial.Serial(ARD_SERIAL_PORT, ARD_BD)
        logger.info('Connecto to arduino port: ' + ARD_SERIAL_PORT)
    except Exception:
        err = sys.exc_info()[0]
        logger.error(err)
        #logger.findCaller(stack_info=True)
    return ser


if __name__ == '__main__':
    main()
