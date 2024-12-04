from flask import Blueprint, jsonify, request, make_response
from models import ExtraInformation, ExtraInformationSchema, db

extra_info_routes = Blueprint('extra_info_routes', __name__)

@extra_info_routes.route('/extra_information', methods=['GET'])
def get_all_extra_information():
    all_info = ExtraInformation.query.all()
    schema = ExtraInformationSchema(many=True)
    return make_response(jsonify(schema.dump(all_info)), 200)

@extra_info_routes.route('/extra_information/<string:user_id>', methods=['GET'])
def get_extra_information_by_user(user_id):
    info = ExtraInformation.query.get(user_id)
    if info:
        schema = ExtraInformationSchema()
        return jsonify(schema.dump(info)), 200
    return make_response(jsonify({'message': 'Extra information not found'}), 404)

@extra_info_routes.route('/extra_information', methods=['POST'])
def create_extra_information():
    data = request.get_json()
    try:
        new_info = ExtraInformationSchema().load(data)
        extra_info = ExtraInformation(**new_info)
        db.session.add(extra_info)
        db.session.commit()
        schema = ExtraInformationSchema()
        return make_response(jsonify(schema.dump(extra_info)), 201)
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({'error': str(e)}), 500)

@extra_info_routes.route('/extra_information/<string:user_id>', methods=['PUT'])
def update_extra_information(user_id):
    info = ExtraInformation.query.get(user_id)
    if info:
        data = request.get_json()
        info.type = data.get('type', info.type)
        info.information = data.get('information', info.information)
        db.session.commit()
        return make_response(jsonify({'message': 'Extra information updated successfully'}), 200)
    return make_response(jsonify({'message': 'Extra information not found'}), 404)

@extra_info_routes.route('/extra_information/<string:user_id>', methods=['DELETE'])
def delete_extra_information(user_id):
    info = ExtraInformation.query.get(user_id)
    if info:
        db.session.delete(info)
        db.session.commit()
        return make_response(jsonify({'message': 'Extra information deleted successfully'}), 200)
    return make_response(jsonify({'message': 'Extra information not found'}), 404)
