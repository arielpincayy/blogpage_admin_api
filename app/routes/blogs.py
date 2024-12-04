from flask import Blueprint, jsonify, request, make_response
from models import Blogs, BlogSchema, db

blog_routes = Blueprint('blog_routes', __name__)

@blog_routes.route('/blogs', methods=['GET'])
def get_all_blogs():
    blogs = Blogs.query.all()
    schema = BlogSchema(many=True)
    return make_response(jsonify(schema.dump(blogs)), 200)

@blog_routes.route('/blog/<string:blog_id>', methods=['GET'])
def get_blog_by_id(blog_id):
    blog = Blogs.query.get(blog_id)
    if blog:
        schema = BlogSchema()
        return make_response(jsonify(schema.dump(blog)), 200)
    return make_response(jsonify({'message': 'Blog not found'}), 404)

@blog_routes.route('/blogs', methods=['POST'])
def create_blog():
    data = request.get_json()
    try:
        new_blog = BlogSchema().load(data)
        blog = Blogs(**new_blog)
        db.session.add(blog)
        db.session.commit()
        schema = BlogSchema()
        return make_response(jsonify(schema.dump(blog)), 201)
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({'error': str(e)}), 500)

@blog_routes.route('/blog/<string:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    blog = Blogs.query.get(blog_id)
    if blog:
        data = request.get_json()
        blog.title = data.get('title', blog.title)
        blog.keywords = data.get('keywords', blog.keywords)
        db.session.commit()
        return make_response(jsonify({'message': 'Blog updated successfully'}), 200)
    return make_response(jsonify({'message': 'Blog not found'}), 404)

@blog_routes.route('/blog/<string:blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    blog = Blogs.query.get(blog_id)
    if blog:
        db.session.delete(blog)
        db.session.commit()
        return make_response(jsonify({'message': 'Blog deleted successfully'}), 200)
    return make_response(jsonify({'message': 'Blog not found'}), 404)
