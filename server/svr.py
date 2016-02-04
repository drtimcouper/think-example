import json

from flask import Flask

app = Flask(__name__)

@app.route('/json')
def data_json():

    return json.dumps({'data': ['123', 'me']})


if __name__ == '__main__':
    app.run()
