from functools import wraps
from flask import request, Response, current_app

def checkingAuth(username, password):
    """This function is called to check if a username and/or a password 
    combination is valid.
    """
    return username == current_app.config['ADMIN_USERNAME'] \
        and password == current_app.config['ADMIN_PASSWORD']

def authenticate():
    """Sending a 401 response that enables basic authentication """
    return Response(
    'Sorry, sir, we could not verify your access level for that URL address.\n'
    'You must login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not checkingAuth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated