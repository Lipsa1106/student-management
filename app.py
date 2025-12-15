from flask import Flask
from config import Config
from extensions import db, migrate
from student.routes import student_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    print("migration Done..")
    app.register_blueprint(student_bp, url_prefix="/student")
    print("Blue print is Ready")
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
