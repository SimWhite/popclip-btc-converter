#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
import os

popclip_text = os.getenv('POPCLIP_TEXT')


def coins_price():
    req = urllib2.urlopen('https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC&tsyms=USD,EUR,RUB')
    parsed_req = json.load(req)

    parsed_req = '€{:.2f} / ${:.2f} / {:.2f}₽'.format(
        round(parsed_req['BTC']['EUR'] * float(popclip_text), 2),
        round(parsed_req['BTC']['USD'] * float(popclip_text), 2),
        round(parsed_req['BTC']['RUB'] * float(popclip_text), 2))

    return parsed_req

print coins_price()
