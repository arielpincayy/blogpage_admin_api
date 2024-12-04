from flask import Blueprint, jsonify, request, make_response
from models import Contents, ContentSchema, db

content_routes = Blueprint('content_routes', __name__)

@content_routes.route('/contents', methods=['GET'])
def get_all_contents():
    contents = Contents.query.all()
    schema = ContentSchema(many=True)
    return make_response(jsonify(schema.dump(contents)), 200)

@content_routes.route('/content/<string:blog_id>', methods=['GET'])
def get_content_by_blog_id(blog_id):
    content = Contents.query.filter_by(blog_ID=blog_id).all()
    if content:
        schema = ContentSchema(many=True)
        return make_response(jsonify(schema.dump(content)), 200)
    return make_response(jsonify({'message': 'Content not found'}), 404)

@content_routes.route('/contents', methods=['POST'])
def create_content():
    data = request.get_json()
    try:
        new_content = ContentSchema().load(data)
        content = Contents(**new_content)
        db.session.add(content)
        db.session.commit()
        schema = ContentSchema()
        return make_response(jsonify(schema.dump(content)), 201)
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({'error': str(e)}), 500)

@content_routes.route('/content/<string:blog_id>', methods=['DELETE'])
def delete_content(blog_id):
    content = Contents.query.filter_by(blog_ID=blog_id).all()
    if content:
        for c in content:
            db.session.delete(c)
        db.session.commit()
        return make_response(jsonify({'message': 'Content deleted successfully'}), 200)
    return make_response(jsonify({'message': 'Content not found'}), 404)
