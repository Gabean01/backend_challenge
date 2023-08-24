from flask import request, jsonify, abort
from flask_restx import Api, Resource
from app import app, db
from app.models import User, Post, Comment

#USERS

users_ns = Namespace('users', description='User related operations')

@users_ns.route('/')
class UsersResource(Resource):
    @users_ns.doc(description="Gets all users")
    def get(self):
        users = User.query.all()
        user_list = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
        return jsonify(user_list)

    @users_ns.doc(description="Create a new user")
    @users_ns.expect(user_model)  
    def post(self):
        data = request.get_json()
        if "username" not in data or "email" not in data:
            return jsonify({"error": "Missing username or email"}), 400

        new_user = User(username=data["username"], email=data["email"])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201


@users_ns.route('/<int:user_id>')
class UserResource(Resource):
    @users_ns.doc(description="Gets a user by ID")
    @users_ns.param('user_id')
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            abort(404)
        return jsonify({"id": user.id, "username": user.username, "email": user.email}) 


@users_ns.doc(description="Update a user by ID")
    @users_ns.param('user_id')
    @users_ns.expect(user_model)  
    def put(self, user_id):
        user = User.query.get(user_id)
        if not user:
            abort(404)

        data = request.get_json()
        if "username" not in data or "email" not in data:
            return jsonify({"error": "Missing username or email"}), 400

        user.username = data["username"]
        user.email = data["email"]
        db.session.commit()
        return jsonify({"message": "User updated successfully"})


 @users_ns.doc(description="Delete a user by ID")
    @users_ns.param('user_id')
    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            abort(404)

        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"})



#POSTS

posts_ns = Namespace('posts', description='Post-Related Operations')

@posts_ns.route('/')
class PostsResource(Resource):
    @posts_ns.doc(description="Obtiene todas las publicaciones")
    def get(self):
        posts = Post.query.all()
        post_list = [{"id": post.id, "title": post.title, "content": post.content} for post in posts]
        return jsonify(post_list)


    @posts_ns.doc(description="Create a new post")
    @posts_ns.expect(post_model)  
    def post(self):
        data = request.get_json()
        if "title" not in data or "content" not in data:
            return jsonify({"error": "Missing title or content"}), 400

        new_post = Post(title=data["title"], content=data["content"])
        db.session.add(new_post)
        db.session.commit()
        return jsonify({"message": "Post created successfully"}), 201

@posts_ns.route('/<int:post_id>')
class PostResource(Resource):
    @posts_ns.doc(description="Get a post by ID")
    @posts_ns.param('post_id')
    def get(self, post_id):
        post = Post.query.get(post_id)
        if not post:
            abort(404)
        return jsonify({"id": post.id, "title": post.title, "content": post.content}) 


    @posts_ns.doc(description="Update a post by ID")
    @posts_ns.param('post_id')
    @posts_ns.expect(post_model)  
    def put(self, post_id):
        post = Post.query.get(post_id)
        if not post:
            abort(404)

        data = request.get_json()
        if "title" not in data or "content" not in data:
            return jsonify({"error": "Missing title or content"}), 400

        post.title = data["title"]
        post.content = data["content"]
        db.session.commit()
        return jsonify({"message": "Post updated successfully"})



    @posts_ns.doc(description="Delete a post by ID")
    @posts_ns.param('post_id')
    def delete(self, post_id):
        post = Post.query.get(post_id)
        if not post:
            abort(404)

        db.session.delete(post)
        db.session.commit()
        return jsonify({"message": "Post deleted successfully"})



#COMMENTS

comments_ns = Namespace('comments', description='Comment Related Operations')

@comments_ns.route('/')
class CommentsResource(Resource):
    @comments_ns.doc(description="Gets all comments")
    def get(self):
        comments = Comment.query.all()
        comment_list = [{"id": comment.id, "text": comment.text} for comment in comments]
        return jsonify(comment_list)

    @comments_ns.doc(description="Create a new comment")
    @comments_ns.expect(comment_model)  
    def post(self):
         data = request.get_json()
        if "text" not in data:
            return jsonify({"error": "Missing text"}), 400

        new_comment = Comment(text=data["text"])
        db.session.add(new_comment)
        db.session.commit()
        return jsonify({"message": "Comment created successfully"}), 201


@comments_ns.route('/<int:comment_id>')
class CommentResource(Resource):
    @comments_ns.doc(description="Gets a comment by ID")
    @comments_ns.param('comment_id')
    def get(self, comment_id):
        comment = Comment.query.get(comment_id)
        if not comment:
            abort(404)
        return jsonify({"id": comment.id, "text": comment.text}) 


@comments_ns.doc(description="Update a comment by ID")
    @comments_ns.param('comment_id')
    @comments_ns.expect(comment_model)  
    def put(self, comment_id):
         comment = Comment.query.get(comment_id)
        if not comment:
            abort(404)

        data = request.get_json()
        if "text" not in data:
            return jsonify({"error": "Missing text"}), 400

        comment.text = data["text"]
        db.session.commit()
        return jsonify({"message": "Comment updated successfully"})



    @comments_ns.doc(description="Delete a comment by ID")
    @comments_ns.param('comment_id')
    def delete(self, comment_id):
        comment = Comment.query.get(comment_id)
        if not comment:
            abort(404)

        db.session.delete(comment)
        db.session.commit()
        return jsonify({"message": "Comment deleted successfully"})