from flask import Flask, render_template
from flask_socketio import SocketIO

SERVER_HOSTNAME = ''
SERVER_PORT = 5000

# gunicorn *requires* the name 'application', at least by default.
application = Flask(__name__)
# flask will give preference to eventlet simply by virtue of it being installed on the system.
# It need not be imported or even specified using async_mode!
socketio = SocketIO(application, async_mode='eventlet')

@application.route('/')
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
    print('Do not run this script directly!')
    print('')
    print('Instead, debug using:')
    print('$ export FLASK_APP={}'.format(__file__))
    print('$ export FLASK_ENV=development')
    print('$ flask run --port=8000')
    print('')
    print('and deploy using:')
    print('$ gunicorn --worker-class eventlet --workers 1 app')
    print('')
    print('Then browse to:')
    print('localhost:8000')
