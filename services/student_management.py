from operator import or_

from models.student import Student
from extensions import db


class StudentManagement:
    def add_student(self, name, roll_no):
        print(name)
        if Student.query.filter(
                or_(Student.name == name, Student.rollno == roll_no)
        ).first():
            return {
                "success": False,
                "message": f"Student with name {name} or {roll_no} already exists"
            }
        student = Student(name=name, rollno=roll_no)
        db.session.add(student)
        db.session.commit()
        return {
            "success": True,
            "message": "Student added successfully",
            "student": Student.to_dict(student)
        }

    def get_students(self):
        students = Student.query.all()
        students_list = []
        for student in students:
            students_list.append(student.to_dict())
        return {
            "success": True,
            "students": students_list
        }

    def delete_student(self, id):
        existing_student = Student.query.filter_by(id=id).first()
        if existing_student:
            db.session.delete(existing_student)
            db.session.commit()
            return {
                "success": True,
                "message": "Student deleted successfully"
            }
        else:
            return {
                "success": False,
                "message": "Student with roll_no does not exist"
            }

    def update_student(self, id, name, roll_no):
        existing_student = Student.query.filter_by(id=id).first()
        if existing_student:
            existing_student.name = name
            existing_student.rollno = roll_no
            db.session.commit()
            return {
                "success": True,
                "message": "Student updated successfully"
            }
        else:
            return {
                "success": False,
                "message": "Student with id does not exist"
            }

    def get_student(self, id):
        existing_student = Student.query.filter_by(id=id).first()
        if existing_student:
            return {
                "success": True,
                "message": "Student with id exist",
                "student": Student.to_dict(existing_student),
            }
        else:
            return {
                "success": False,
                "message": "Student with id does not exist"
            }

    def search_student(self, name):
        existing_student = Student.query.filter_by(name=name).first()
        if existing_student:
            return {
                "success": True,
                "message": "Student Found",
                "student": Student.to_dict(existing_student)
            }
        else:
            return {
                "success": False,
                "message": "Student not found"
            }
