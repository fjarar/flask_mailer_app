import os

from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE=os.environ.get('FLASK_DATABASE'),
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_PORT=os.environ.get('FLASK_DATABASE_PORT'), 
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        FROM_EMAIL=os.environ.get('FROM_EMAIL'),
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SENDGRID_KEY=os.environ.get('SENDGRID_API_KEY')
                    
    )

    from . import db

    db.init_app(app)

    from . import mail

    app.register_blueprint(mail.bp)
    return app