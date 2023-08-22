from flask import request, jsonify, abort
from app import app, db
from app.models import User, Post, Comment

#USERS

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return jsonify(user_list)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404)
    return jsonify({"id": user.id, "username": user.username, "email": user.email}) 


@app.route('/users', methods=['POST']) 
def created_user():
    data = request.get_json()
    if "username" not in data or "email" not in data:
        return jsonify({"error": "Missing username or email"}), 400

    new_user = User(username=data["username"], email=data["email"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
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


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404)

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"})



#POSTS

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    post_list = [{"id": post.id, "title": post.title, "content": post.content} for post in posts]
    return jsonify(post_list)


@app.route('/posts/<int:post_id>', methods=['GET'])   
 def get_posts():
    posts = Post.query.get(post_id)
    if not post:
        abort(400)
    return jsonify({"id": post.id, "title": post.title, "content": post.content} for post in posts)


@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    if "title" not in data or "content" not in data:
        return jsonify({"error": "Missing title or content"}), 400

    new_post = Post(title=data["title"], content=data["content"])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created successfully"}), 201


@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
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


@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        abort(404)

    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted successfully"})


#COMMENTS

@app.route('/comments', methods=['GET'])
def get_comments():
    comments = Comment.query.all()
    comment_list = [{"id": comment.id, "text": comment.text} for comment in comments]
    return jsonify(comment_list)


@app.route('/comments/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if not comment:
        abort(404)
    return jsonify({"id": comment.id, "text": comment.text})


@app.route('/comments', methods=['POST'])
def create_comment():
    data = request.get_json()
    if "text" not in data:
        return jsonify({"error": "Missing text"}), 400

    new_comment = Comment(text=data["text"])
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"message": "Comment created successfully"}), 201


@app.route('/comments/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if not comment:
        abort(404)

    data = request.get_json()
    if "text" not in data:
        return jsonify({"error": "Missing text"}), 400

    comment.text = data["text"]
    db.session.commit()
    return jsonify({"message": "Comment updated successfully"})


@app.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if not comment:
        abort(404)

    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "Comment deleted successfully"})