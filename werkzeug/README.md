# Flask-SocketIO with Werkzeug

Run flask served by Werkzeug's dev server:
```
$ FLASK_ENV=development
# flask auto-detects app.py
$ flask run
```
Only viable for debug mode - in production mode it fails and I don't know why.
Wrapping the flask app in the SocketIO app seems to cause this issue.

Alternatively, run manually:
```
$ python index.py
```
"production" or debug.


Will fail if in production environment because eventlet/gevent aren't installed in the venv.
