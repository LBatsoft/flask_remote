from functools import wraps
from flask import session, abort, redirect, url_for


def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get('is_manager', None):
            abort(403)
        return f(*args, **kwargs)

    return wrapper


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('is_login'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for("user.login"))

    return wrapper


def validate_forms(forms):
    flag = True
    for f in forms:
        if not f.validate_on_submit():
            flag = False
    return flag
