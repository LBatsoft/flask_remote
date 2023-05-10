from flask import Flask
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import find_modules, import_string

csrf = CSRFProtect()


class ReverseProxyMiddleware(object):

    def __init__(self, app, script_name):
        self.app = app
        self.script_name = script_name

    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = self.script_name
        if environ['PATH_INFO'].startswith(self.script_name):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.script_name):]
        return self.app(environ, start_response)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bugaosuni'  # A secret key is required to use CSRF.
    csrf.init_app(app)

    # app.config["SQLALCHEMY_POOL_RECYCLE"] = 3000
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_pre_ping": True,
        # "pool_recycle": 86000
    }

    @app.add_template_filter
    def show_content(content):
        return content[:140] + ("..." if len(content) > 140 else "")

    for path in find_modules('app.handlers'):
        name = path.rsplit('.')[-1]
        module = import_string(path)
        if hasattr(module, '%s_bp' % name):
            bp = getattr(module, '%s_bp' % name)
            app.register_blueprint(bp)

    app.logger.setLevel("INFO")  # TODO: 显示请求日志

    return app
