#!/usr/bin/env python

import httplib
import json

domain = "btc-e.com"
path = "/api/2/"
coins = ["btc/usd", "ltc/btc", "ltc/usd", "nmc/btc", "nmc/usd", "nvc/btc",
         "nvc/usd", "trc/btc", "ppc/btc", "ppc/usd", "ftc/btc", "xpm/btc"]

# String -> Json
# return the json based on a given coin
def get_ticker(coin):
    c = httplib.HTTPSConnection(domain)
    c.request("GET", ''.join((path, coin.replace("/", "_"), "/ticker")))
    response = c.getresponse()
    return response.read()

# Json -> String
# parse json to string for output
def parse_json(data):
    d = json.loads(data)
    options = ['buy', 'sell', 'high', 'low']
    d = [str(d['ticker'][x]) for x in options]
    d = [round(float(x), 2) if d[0][0] != '0' else "%.2E" % float(x) for x in d]
    return ' '.join([''.join((x, ': ', str(y))) for x, y in zip(options, d)])

def btce(jenni, input):
    split = input.group().split(' ')

    if len(split) == 1:
        return jenni.say('try .btc-e help')

    elif split[1] in coins:
        reply = parse_json(get_ticker(split[1]))
        jenni.say(reply)

    elif split[1] == 'help':
        options = ', '.join(coins)
        jenni.msg(input.nick, "Try .btc-e and one of the following options: ")
        jenni.msg(input.nick, options)

btce.commands =['btc-e']
btce.priority = 'high'

if __name__ == '__main__':
    print __doc__.strip()


