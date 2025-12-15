from flask import Blueprint, request, jsonify

from services.student_management import StudentManagement

student_bp = Blueprint("student", __name__)
management = StudentManagement()


@student_bp.route("/", methods=["GET", "POST"])
def student_list_create():
    if request.method == "GET":
        try:
            result = management.get_students()
            return jsonify(result)
        except Exception as e:
            return jsonify({
                "message": "Something went wrong",
                "error": str(e)  # actual error message
            }), 500
    elif request.method == "POST":
        data = request.json
        if not data or not "name" in data or not "roll_no" in data:
            return jsonify({"message": "Missing data"}), 400
        try:
            data["roll_no"] = int(data["roll_no"])
        except ValueError:
            return jsonify({"message": "Invalid roll_no"}), 400

        try:
            result = management.add_student(data["name"], data["roll_no"])
            if result["success"]:
                return jsonify(result), 201
            else:
                return jsonify(result), 400
        except ValueError:
            return jsonify({"message": "Invalid roll_no"}), 400

        except Exception as e:
            return jsonify({
                "message": "Something went wrong",
                "error": str(e)  # actual error message
            }), 500
    else:
        return jsonify({})


@student_bp.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
def student_delete_get_put(id):
    if not id:
        return jsonify({"message": "Missing parameter"}), 400
    else:
        if request.method == "DELETE":
            try:
                result = management.delete_student(id)
                if result["success"]:
                    return jsonify(result), 200
                else:
                    return jsonify(result), 404
            except Exception as e:
                return jsonify({
                    "message": "Something went wrong",
                    "error": str(e)  # actual error message
                }), 500
        elif request.method == "GET":
            try:
                result = management.get_student(id)
                if result["success"]:
                    return jsonify(result), 200
                else:
                    return jsonify(result), 400
            except Exception as e:
                return jsonify({
                    "message": "Something went wrong",
                    "error": str(e)
                }), 500
        elif request.method == "PUT":
            data = request.json
            print(data)
            if not data or "name" not in data or "roll_no" not in data:
                return jsonify({"message": "Missing data"}), 400
            try:
                result = management.update_student(id, data["name"], data["roll_no"])
                if result["success"]:
                    return jsonify(result), 200
                else:
                    return jsonify(result), 400
            except Exception as e:
                return jsonify({"message": "Something went wrong", "error": str(e)}), 500
        else:
            return jsonify({})


@student_bp.route("/search", methods=["GET"])
def student_list_search():
    name = request.args["name"]
    if not name or not isinstance(name, str):
        return jsonify({"message": "Invalid parameters"}), 400
    try:
        result = management.search_student(name)
        if result["success"]:
            return jsonify(result), 200
        else:
            return jsonify(result), 404
    except Exception as e:
        return jsonify({"message": "Something went wrong", "error": str(e)}), 500
