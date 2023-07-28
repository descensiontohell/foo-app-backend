from flask import request
from flask_restx import Namespace, Resource
from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import BadRequest

from api.schemas import PostSchema
from api.services.posts import post_service


posts_bp = Namespace("posts", path="/api/posts")
post_schema = PostSchema()


@posts_bp.route("/")
class PostResource(Resource):
    def get(self, **_):
        posts = post_service.get_all()

        return post_schema.dump(posts, many=True)

    def post(self, **_):
        try:
            new_post = PostSchema().load(request.json)
        except ValidationError:
            raise BadRequest("Both name and description fields are required")

        post = post_service.create(new_post)

        return post_schema.dump(post)
