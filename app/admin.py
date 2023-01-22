from app import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from app.models.Articles import Articles
from app.models.Authors import Authors
from app.models.Tags import Tags
from app.models.User import User


class CustomModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.email == "test@test.com"


admin = Admin(app)
admin.add_view(CustomModelView(Articles, db.session))
admin.add_view(CustomModelView(Authors, db.session))
admin.add_view(CustomModelView(Tags, db.session))
admin.add_view(CustomModelView(User, db.session))
