import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'topicroutes.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False # Disable Flask-SQLAlchemy's event tracking. (http://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications)

WTF_CSRF_ENABLED = True
SECRET_KEY = '{3E3844DA-9298-4A0F-85FF-651A13A4B89F}'
