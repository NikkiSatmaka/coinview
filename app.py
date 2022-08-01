import requests
import config
import csv
from binance.client import Client
from binance.enums import *
from flask import Flask, render_template, request, flash, redirect, jsonify

app = Flask(__name__)
app.secret_key = b'ssssfasdfasdfas09d8f7a0s9dg8703984'

client = Client(config.API_KEY, config.API_SECRET)

@app.route("/")
def index():
    title = 'CoinView'

    account = client.get_account()

    balances = account['balances']

    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']

    return render_template('index.html', title=title, my_balances=balances, symbols=symbols)

@app.route("/buy", methods=['POST'])
def buy():
    print(request.form)
    try:
        # order = client.create_test_order(
        order = client.create_order(
            symbol=request.form['symbol'],
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=request.form['quantity'])
    except Exception as e:
        flash(e.message, "error")

    return redirect('/')


@app.route("/sell")
def sell():
    return "sell"

@app.route("/settings")
def settings():
    return "settings"

@app.route("/history")
def history():
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Oct, 2021")

    cols = ['time', 'open', 'high', 'low', 'close']

    processed_candlesticks = [dict(zip(cols, data[:5])) for data in candlesticks]

    for candlestick in processed_candlesticks:
        candlestick['time'] = candlestick['time'] / 1000

    return jsonify(processed_candlesticks)
