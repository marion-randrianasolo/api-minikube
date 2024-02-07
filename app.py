from flask import Flask, jsonify
import os
import threading
import signal

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify(status="success", message="200 OK")


def shutdown_server():
    os.kill(os.getpid(), signal.SIGINT)


@app.route('/exit')
def exit_server():
    shutdown_server()
    return jsonify(status="success", message="Server is shutting down...")


@app.route('/cpu')
def cpu_load():
    def cpu_stress():
        while True:
            pass

    thread = threading.Thread(target=cpu_stress)
    thread.start()
    return jsonify(status="success", message="CPU load started")


if __name__ == '__main__':
    app.run(debug=True)
