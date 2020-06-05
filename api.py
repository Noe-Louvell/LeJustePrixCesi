#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json, random
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route('/')
def index():
    ApiKey = "49b27112-58be-47e3-b681-60cb722c0755",
    randNumbObject = random.randint(1, 20)
    url = "https://api.cdiscount.com/OpenApi/json/Search"

    params = {
            "ApiKey": ApiKey,
            "SearchRequest": {
                "Keyword": "phone",
                "Pagination": {
                    "ItemsPerPage": randNumbObject,
                    "PageNumber": 1
                },
                "Filters": {
                    "Price": {
                        "Min": 0,
                        "Max": 0
                    },
                    "Navigation": "clavier",
                    "IncludeMarketPlace": "false"
                }
            }
        }
    r = requests.post(url, data=json.dumps(params))
    name = (r.json()['Products'][0]['Name'])
    price = (r.json()['Products'][0]['BestOffer']['SalePrice'])

    return render_template("main.html", NAME=name, PRICE=price)


if __name__ == "__main__":
    app.run()
