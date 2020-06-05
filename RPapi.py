#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json, random, time
from flask import Flask, render_template, request


app = Flask(__name__, template_folder="templates")


@app.route("/", methods=['POST', 'GET'])
def index():
    attempt = []
    begin = time.time()
    userPrice = -20
    randNumb = random.randint(1, 20)

    if request.method == "POST":
        randNumb = int(request.form["randNumb"])
        userPrice = int(request.form["priceForm"])
        attempt = json.loads(request.form["attempt"])
        attempt.append(userPrice)

    ApiKey = "49b27112-58be-47e3-b681-60cb722c0755",
    url = "https://api.cdiscount.com/OpenApi/json/Search"
    params = {
            "ApiKey": ApiKey,
            "SearchRequest": {
                "Keyword": "sac",
                "Pagination": {
                    "ItemsPerPage": randNumb,
                    "PageNumber": 1
                },
                "Filters": {
                    "Price": {
                        "Min": 0,
                        "Max": 0
                    },
                    "Navigation": "",
                    "IncludeMarketPlace": "false"
                }
            }
        }
    r = requests.post(url, data=json.dumps(params))
    name = (r.json()['Products'][0]['Name'])
    price = int(float(r.json()['Products'][0]['BestOffer']['SalePrice']))
    image = (r.json()['Products'][0]['MainImageUrl'])

    return render_template("main.html", NAME=name, PRICE=price, IMAGE=image, USERPRICE=userPrice, BEGIN=begin, RANDNUMB=randNumb, ATTEMPT=attempt)


if __name__ == "__main__":
    app.run()
    Bootstrap(app)
