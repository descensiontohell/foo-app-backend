from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
mg = Migrate()


def setup_db(app: Flask):
    db.init_app(app)
    mg.init_app(app, db)


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<{self.name} ({self.id})>"
