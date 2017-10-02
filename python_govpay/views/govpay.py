import flask
from flask import request, Blueprint, Response, render_template, redirect
from flask import current_app, g
import datetime
import json
import random
import requests

# This is the blueprint object that gets registered into the app in blueprints.py.
govpay = Blueprint('govpay', __name__)


@govpay.route("/govpay")
def check_status():
    return Response(response=json.dumps({
        "route": "govpay",
        "status": "OK"
    }), mimetype='application/json', status=200)


@govpay.route("/index")
def index():
    return render_template(
        'index.html',
        title='Python - Govpay',
        # things=things
    )


@govpay.route("/purchase", methods=['POST'])
def purchase():
    data = {}
    reference = random.randint(1000000, 9999999)
    data['amount'] = int(request.form['amount'])
    data['reference'] = str(reference)
    data['description'] = 'FPI Title Summary Purchase'
    data['return_url'] = 'https://localhost:9999/completed/?ref={}'.format(reference)
    # json_data = json.dumps(data)
    # print(json_data)
    url = 'https://publicapi.payments.service.gov.uk/v1/payments'

    api_key = ''
    search_headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer {}'.format(api_key)
    }
    print(search_headers)
    resp = requests.post(url,
                         data=json.dumps(data),
                         headers=search_headers)
    resp_dict = resp.json()
    pay_url = resp_dict['_links']['next_url']['href']
    print(pay_url)
    return redirect(pay_url, code=302)


@govpay.route("/completed")
def completed():
    price = 'hello'
    return str(price)
