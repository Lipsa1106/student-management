from flask import Blueprint, request, jsonify
from services.user_management import UserManagement

user_bp = Blueprint('user', __name__)
user_management = UserManagement()


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or not "email" in data or not "password" in data:
        return jsonify({"message": "Missing data"}), 400

    if data["email"] and data["password"]:
        try:
            result = user_management.login(data["email"], data["password"])
            if result["status"]:
                return jsonify(result), 200
            else:
                return jsonify(result), 400
        except Exception as e:
            print(e)
            return jsonify({
                "status": False,
                "message": "Login Failed",
                "data": str(e)
            })
    else:
        return jsonify({
            "status": False,
            "message": "Invalid Credentials",
        }), 400


@user_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data or "email" not in data or "name" not in data or "password" not in data or "c_password" not in data or "role" not in data:
        return jsonify({
            "status": False,
            "message": "Invalid data",
        }), 400
    try:
        result = user_management.register(data["name"], data['email'], data['password'], data['c_password'],
                                          data['role'])
        if result["status"]:
            return jsonify(result), 201
        else:
            return jsonify(result), 409
    except Exception as e:
        return jsonify({
            "status": False,
            "message": "Register Failed",
            "data": str(e)
        })
