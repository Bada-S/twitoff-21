# main app/routing file for twitoff

from flask import Flask
from .models import DB, User, Tweet

def create_app():
    app = Flask(__name__)

    app.config("SQLAlchemy_DATABASE_URI") = "sqlite:///db.sqlite3"
    app.config("SQLAlCHEMY_TRACK_MODIFICATIONS") = False

    @app.route('/')
    def root():
        # SQl equivalent = "SELECT * FROM user;"
        user = User.query.all()
        return render_template(base.html, title="Home", user=users)

    @app.route('/reset')
    def reset():
        return "reset endpoint"


    return app
