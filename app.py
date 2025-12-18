from flask import Flask
from flasgger import Swagger


from config import Config
from extensions import db, migrate,jwtManager
from student.routes import student_bp
from user.routes import user_bp
app = Flask(__name__)
Swagger(app)

def create_app():
    
    app.config.from_object(Config)
    jwt_manager = jwtManager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    print("migration Done..")
    app.register_blueprint(student_bp, url_prefix="/student")
    app.register_blueprint(user_bp, url_prefix="/auth")
    print("Blue print is Ready")
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
