import json
from flask import Flask
# from flask_script import Manager
from flask.templating import render_template
# from multiprocessing import managers

# from pip._vendor.cachecontrol import controller

# from server.web_app import persistence
# from datetime import datetime
from datetime import timedelta
from datetime import date

from server.web_app.persistence import get_temperatures_from_to
from server.web_app.persistence import get_hours_from_to
from raspi.controller_LM35 import connect_db

app = Flask(__name__)


# manager = Manager(app)


# @app.route('/temperatures/<int:horas>')
@app.route('/grafica/')
# def hello_world1(horas):
def hello_world1():
    today = date.today()
    # fd = today - timedelta(hours=horas)
    fd = today - timedelta(days=1)
    temps = get_temperatures_from_to(cnx, fd, today)
    hours = get_hours_from_to(cnx, fd, today)
    print(temps.__len__())
    print(hours.__len__())
    #temps = persistence.get_all_temperatures(conn, from_date=fd, to_date=today)

    # return json.dumps(temps)
    return render_template('grafica.html', temperaturas=temps, listaEjeX=hours)


if __name__ == '__main__':
    cnx = connect_db()

    app.run()
    # manager.run()
