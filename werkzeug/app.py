from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

if __name__ == '__main__':
    # Replaces call to flask's app.run()
    # Runs with Werkzeug if FLASK_ENV=deployment
    # Runs with eventlet or gevent otherwise
    socketio.run(app)
