#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json, random
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=['POST', 'GET'])
def index():
    userPrice = -20
    randNumbObject = random.randint(1, 20)

    if request.method == "POST":
        userPrice = int(request.form["priceForm"])

    ApiKey = "49b27112-58be-47e3-b681-60cb722c0755",
    url = "https://api.cdiscount.com/OpenApi/json/Search"
    params = {
            "ApiKey": ApiKey,
            "SearchRequest": {
                "Keyword": "bouteille",
                "Pagination": {
                    "ItemsPerPage": randNumbObject,
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
    price =int(float(r.json()['Products'][0]['BestOffer']['SalePrice']))
    image = (r.json()['Products'][0]['MainImageUrl'])

    return render_template("main.html", NAME=name, PRICE=price, IMAGE=image, USERPRICE=userPrice)


if __name__ == "__main__":
    app.run()
