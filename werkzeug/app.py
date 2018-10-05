from flask import Flask, render_template
from flask_socketio import SocketIO

SERVER_HOSTNAME = ''
SERVER_PORT = 5000

app = Flask(__name__)
socketio = SocketIO(app, async_mode='threading')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def connect():
    print('connect')

@socketio.on('disconnect')
def disconnect():
    print('disconnect')

# 'message' is the default event for a SocketIO client's send() call.
@socketio.on('message')
def message(data):
    print('message:', data)

# Custom event
@socketio.on('echo')
def echo(data):
    print('echo:', data)
    socketio.emit('echo', data)

@socketio.on('client_callback')
def client_callback(data):
    print('client_callback:', data)
    return 'Server Response 1', 'Server Response 2'

if __name__ == '__main__':
    # Replaces call to flask's app.run()
    # Runs with Werkzeug if FLASK_ENV=deployment
    # Runs with eventlet or gevent otherwise
    socketio.run(app, host=SERVER_HOSTNAME, port=SERVER_PORT)
