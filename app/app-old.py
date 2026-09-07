from flask import Flask, render_template
from datetime import datetime
import platform
import socket
import os
import random

app = Flask(__name__)

def get_application_info():
    """
    Obtém informações da instância onde a aplicação está executando.
    No OpenShift, o hostname normalmente corresponde ao nome do Pod.
    """

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
    """
    Endpoint que retorna as informações da instância
    em formato JSON.
    """

    hostname, ip_address = get_application_info()

    return {
        "hostname": hostname,
        "ip": ip_address,
        "port": 3333
    }

@app.route("/health")
def health():
    """
    Endpoint simples para verificar se a aplicação está ativa.
    """

    return {
        "status": "OK"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3333, debug=True)
