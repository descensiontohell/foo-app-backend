from api.models import Post, db


class PostService:
    def get_all(self) -> list[Post]:
        return Post.query.order_by(Post.id.desc()).all()

    def create(self, obj: Post) -> Post:
        db.session.add(obj)
        db.session.commit()
        db.session.refresh(obj)

        return obj


post_service = PostService()
