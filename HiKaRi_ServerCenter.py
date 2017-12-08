from flask import Flask, request, abort, render_template
from Content.ExecutiveSword import ExecutiveSword
from Content.Data import Service
from Tools.Fc import Fc
from Log.Logger import Logger
from Config import *
import json

app = Flask(__name__)
es = ExecutiveSword()
logger = Logger("Main")


@app.route('/', methods=['GET'])
def test():
    return render_template("test.html",info=es.show())


# @app.route('/api/registered', methods=['POST'])
@app.route('/api/registered', methods=['POST'])
def response_registered():
    if request.method == 'POST':
        r = request
        name = r.form['name']
        host = r.form['host']
        port = r.form['port']
        service = Service("HiKaRi_Server", -0.01,
                          name,
                          host,
                          port)
        es.add(service)
        return 'ok'


@app.route('/api/ask/<name>', methods=['GET'])
def response_ask_get(name):
    return json.dumps(Fc(es.get(name)).map(lambda x: x.toDict()).done())


@app.route('/api/ask', methods=['POST'])
def response_ask_post():
    return json.dumps(Fc(es.get(request.form["name"])).map(lambda x: x.toDict()).done())


@app.errorhandler(404)
def page_not_found(e):
    return '"Null"'


if __name__ == '__main__':
    app.run(port=HIKARI_PORT)
