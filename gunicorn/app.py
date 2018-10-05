from flask import Flask, render_template
from flask_socketio import SocketIO

SERVER_HOSTNAME = ''
SERVER_PORT = 5000

app = Flask(__name__)
# flask will give preference to eventlet simply by virtue of it being installed on the system.
# It need not be imported or even specified using async_mode!
socketio = SocketIO(app, async_mode='eventlet')

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
    import eventlet
    listener = eventlet.listen((SERVER_HOSTNAME, SERVER_PORT))
    # Run the app, not socketio.
    # Rather than wrapping the Flask app,
    # SocketIO() seems to inject itself into the Flask app.
    # Specificially, it loads itself into flask's app.extensions dictionary.
    eventlet.wsgi.server(listener, app)
