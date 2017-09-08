from flask import Flask
import json
app= Flask(__name__)
@app.route('/')
def index():
    x={'a':'loki','b':'lok'}
    return json.dumps(x)
if __name__=="__main__":
    app.run()
