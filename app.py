from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage
students = []

# Home route
@app.route('/')
def home():
    return "Student REST API is Running!"

# CREATE student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json(force=True)

    if not data:
        return jsonify({"error": "No data provided"}), 400

    students.append(data)
    return jsonify({
        "message": "Student added successfully",
        "student": data
    }), 201


# READ all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)


# READ single student
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    if 0 <= student_id < len(students):
        return jsonify(students[student_id])
    return jsonify({"error": "Student not found"}), 404


# UPDATE student
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    if 0 <= student_id < len(students):
        data = request.get_json(force=True)
        students[student_id] = data
        return jsonify({"message": "Student updated successfully"})
    return jsonify({"error": "Student not found"}), 404


# DELETE student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    if 0 <= student_id < len(students):
        deleted = students.pop(student_id)
        return jsonify({"message": "Student deleted", "student": deleted})
    return jsonify({"error": "Student not found"}), 404


if __name__ == '__main__':
    if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)