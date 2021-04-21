from flask import Flask, render_template
import requests
app = Flask(__name__)

atco="490008660N"

@app.route('/')
def hello_world():
    params = {
        'app_id': '41cd49ac',
        'app_key': '8c415e3902409ebb511bffaa9e1b1dcc',
        'group': 'no'
    }
    results = requests.get('http://transportapi.com/v3/uk/bus/stop/' + atco + '/live.json', params=params).json()
    buses = results['departures']['all']

    return render_template('index.html', buses=buses)