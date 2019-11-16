from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def main():
    return "Bot is running..."


@app.route('/Console')
def console():
    return "Console"

def run():
    app.run(host="0.0.0.0", port=8080)


def life():
    server = Thread(target=run)
    server.start()
