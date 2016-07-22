"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

app = Flask(__name__)
app.config.from_object('topicserver.config')
db = SQLAlchemy(app)

admin = Admin(app, name='topicserver', template_mode='bootstrap3')

from topicserver import views, models
from flask_admin.contrib.sqla import ModelView

admin.add_view(ModelView(models.Person, db.session))

#@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for)