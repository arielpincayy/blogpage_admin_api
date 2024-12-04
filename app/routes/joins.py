from flask import Blueprint, jsonify, make_response
from models import Blogs, Categories, Contents, Users, db

join_routes = Blueprint('join_routes', __name__)
@join_routes.route('/blogs-with-authors', methods=['GET'])
def get_blogs_with_authors():
    results = db.session.query(
        Blogs.blog_ID, Blogs.title, Users.name.label('author_name'), Users.lastname.label('author_lastname')
    ).join(Users, Blogs.user_ID == Users.id).all()

    blogs_with_authors = [
        {
            'blog_ID': blog.blog_ID,
            'title': blog.title,
            'author_name': blog.author_name,
            'author_lastname': blog.author_lastname
        }
        for blog in results
    ]
    return make_response(jsonify(blogs_with_authors), 200)


@join_routes.route('/blogs-with-categories', methods=['GET'])
def get_blogs_with_categories():
    results = db.session.query(
        Blogs.blog_ID, Blogs.title, Categories.name.label('category_name')
    ).join(Categories, Blogs.category_ID == Categories.category_ID).all()

    blogs_with_categories = [
        {
            'blog_ID': blog.blog_ID,
            'title': blog.title,
            'category_name': blog.category_name
        }
        for blog in results
    ]
    return make_response(jsonify(blogs_with_categories), 200)

@join_routes.route('/blogs-contents', methods=['GET'])
def get_blogs_with_contents():
    results = db.session.query(
        Blogs.blog_ID, Blogs.title, Users.name.label('author_name'), Contents.type.label('content_type')
    ).join(Users, Blogs.user_ID == Users.id) \
     .join(Contents, Blogs.blog_ID == Contents.blog_ID).all()

    blogs_with_contents = [
        {
            'blog_ID': blog.blog_ID,
            'title': blog.title,
            'author_name': blog.author_name,
            'content_type': blog.content_type
        }
        for blog in results
    ]
    return make_response(jsonify(blogs_with_contents), 200)

@join_routes.route('/auhtor_categories/<int:id>', methods=['GET'])
def get_authors_categories(id):
    results = db.session.query(
        Categories.name.label('Categories')
    ).join(Blogs, Blogs.category_ID == Categories.category_ID) \
     .join(Users, Blogs.user_ID == Users.id).filter(Users.id == id).all()
    
    categories = [result.Categories for result in results]
    return make_response(jsonify(categories), 200)

