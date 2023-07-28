from flask import Flask
from flask_marshmallow import Marshmallow
from marshmallow import post_load

from api.models import Post

ma = Marshmallow()


def setup_marshmallow(app: Flask):
    ma.init_app(app)


class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post

    name = ma.auto_field(validate=lambda x: len(x) > 0)
    description = ma.auto_field(validate=lambda x: len(x) > 0)

    @post_load
    def make_post(self, data, **_):
        return Post(**data)
