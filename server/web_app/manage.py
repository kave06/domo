import json
from flask import Flask
from flask_script import Manager
from flask.templating import render_template
from multiprocessing import managers

import persistence
from datetime import datetime
from datetime import timedelta

app = Flask(__name__)


# manager = Manager(app)


# @app.route('/temperatures/<int:horas>')
@app.route('/grafica/')
# def hello_world1(horas):
def hello_world1():
    now = datetime.now()
    # fd = now - timedelta(hours=horas)
    fd = now - timedelta(1)

    temps = persistence.get_all_temperatures(conn, from_date=fd, to_date=now)
    print(temps.__sizeof__())
    horas = []
    for i in range(0, 24, 2):
        horas.append(i)

    print(horas)
    # print('hola')

    # return json.dumps(temps)
    return render_template('grafica.html', temperaturas=temps, listaEjeX=horas)
    # return 'hello world'


if __name__ == '__main__':
    conn = persistence.crear_conexiones()

    app.run()
    # manager.run()
