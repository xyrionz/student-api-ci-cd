from flask import jsonify
from app import app


@app.route("/health")
def health():
    return jsonify(status="UP")


@app.route("/student/<int:id>")
def get_student(id):
    if id <= 0:
        return jsonify(error="Invalid student ID"), 400

    return jsonify(id=id, name="Student Name", dept="CSE")
