from flask import Flask, render_template, jsonify
from datetime import datetime
import platform
import socket
import os
import random

app = Flask(__name__)

# Estado simples para permitir testes
application_ready = True


def get_application_info():
    hostname = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_address = "IP não identificado"

    return hostname, ip_address


@app.route("/")
def home():
    hostname = socket.gethostname()

    dados = {
        "status": "Sucesso",
        "hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "python": platform.python_version(),
        "sistema": platform.system(),
        "hostname": hostname,
        "pid": os.getpid(),
        "numero": random.randint(1000, 9999)
    }

    return render_template("index.html", dados=dados)


@app.route("/info")
def info():
    hostname, ip_address = get_application_info()

    return {
        "hostname": hostname,
        "ip": ip_address,
        "port": 3333
    }


@app.route("/health/live")
def liveness():
    return jsonify({
        "status": "UP",
        "check": "liveness"
    }), 200


@app.route("/health/ready")
def readiness():
    global application_ready

    if application_ready:
        return jsonify({
            "status": "UP",
            "check": "readiness"
        }), 200

    return jsonify({
        "status": "DOWN",
        "check": "readiness"
    }), 503


@app.route("/health/disable", methods=["POST"])
def disable_health():
    global application_ready

    application_ready = False

    return jsonify({
        "status": "Application marked as NOT READY"
    }), 200


@app.route("/health/enable", methods=["POST"])
def enable_health():
    global application_ready

    application_ready = True

    return jsonify({
        "status": "Application marked as READY"
    }), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=3333,
        debug=False
    )
```
