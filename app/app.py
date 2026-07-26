from flask import Flask, render_template
from datetime import datetime
import platform
import socket
import os
import random

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3333, debug=True)
