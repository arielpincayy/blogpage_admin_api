from flask import Blueprint, jsonify, request, make_response
from models import Categories, CategorySchema, db

category_routes = Blueprint('category_routes', __name__)

@category_routes.route('/categories', methods=['GET'])
def get_all_categories():
    categories = Categories.query.all()
    schema = CategorySchema(many=True)
    return make_response(jsonify(schema.dump(categories)), 200)

@category_routes.route('/category/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
    category = Categories.query.get(category_id)
    if category:
        schema = CategorySchema()
        return make_response(jsonify(schema.dump(category)), 200)
    return make_response(jsonify({'message': 'Category not found'}), 404)

@category_routes.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    try:
        new_category = CategorySchema().load(data)
        category = Categories(**new_category)
        db.session.add(category)
        db.session.commit()
        schema = CategorySchema()
        return make_response(jsonify(schema.dump(category)), 201)
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({'error': str(e)}), 500)

@category_routes.route('/category/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category = Categories.query.get(category_id)
    if category:
        data = request.get_json()
        category.name = data.get('name', category.name)
        db.session.commit()
        return make_response(jsonify({'message': 'Category updated successfully'}), 200)
    return make_response(jsonify({'message': 'Category not found'}), 404)

@category_routes.route('/category/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = Categories.query.get(category_id)
    if category:
        db.session.delete(category)
        db.session.commit()
        return make_response(jsonify({'message': 'Category deleted successfully'}), 200)
    return make_response(jsonify({'message': 'Category not found'}), 404)
