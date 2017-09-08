from flask import Flask
from flask_cors import CORS, cross_origin
import json
app= Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():
    x={'a':'loki','b':'lok'}
    return json.dumps(x)
if __name__=="__main__":
    app.run()
