from flask import Blueprint, jsonify, request, make_response
from models import Users, UserSchema, db
user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['GET'])
def users():
    get_users = Users.query.all()
    user_schema = UserSchema(many=True)
    users = user_schema.dump(get_users)
    return make_response(jsonify({"users":users}))

@user_routes.route('/user/<int:id>', methods=['GET'])
def get_users(id):
    user = Users.query.get(id)
    if user:
        user_schema = UserSchema()
        user_json = user_schema.dump(user)
        return make_response(jsonify(user_json), 200)
    else:
        return make_response(jsonify({'message':'Author not found'}), 404)

@user_routes.route('/users', methods = ['POST'])
def create_users():
    user_data = request.get_json()
    try:
        new_user_data = UserSchema().load(user_data)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)
    
    new_user = Users(**new_user_data)

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({'error': str(e)}), 500)
    
    user_schema = UserSchema()
    user_json = user_schema.dump(new_user)
    return make_response(jsonify(user_json), 201)

@user_routes.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    user = Users.query.get(id)
    if user:
        data = request.get_json()
        user.name = data.get('name', user.name)
        user.lastname = data.get('lastname', user.lastname)
        user.email = data.get('email', user.email)
        user.writer = data.get('writer', user.writer)
        user.username = data.get('username', user.username)

        db.session.commit()
        return make_response(jsonify({'message': 'User updated successfully'}), 200)
    else:
        return make_response(jsonify({'message': 'User not found'}), 404)


@user_routes.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = Users.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return make_response(jsonify({'message': 'User deleted successfully'}), 200)
    else:
        return make_response(jsonify({'error': 'User not found'}), 404)
    