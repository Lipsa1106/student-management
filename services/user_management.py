import bcrypt

from models import Users
from extensions import db, jwtManager
from utils.jsw_utils import create_token


class UserManagement:
    def login(self, email, password):
        user = Users.query.filter_by(email=email).first()
        if user is None:
            return {
                'status': False,
                'message': 'User Not Found'
            }
        else:
            password_valid = bcrypt.checkpw(
                password.encode("utf-8"),
                user.password  # hashed bytes
            )
            if password_valid:
                try:
                    token = create_token(user.id, user.name, user.email, user.role)

                    return {
                        'status': True,
                        'token': token,
                        'user': {
                            'id': user.id,
                            'name': user.name,
                            'email': user.email,
                            'role': user.role
                        },
                    }
                except Exception as e:
                    return {
                        'status': False,
                        'message': str(e)
                    }
            return {
                'status': True,
                'message': 'Invalid credentials'
            }

    def register(self, name, email, password, c_password, role):
        if password != c_password:
            return {
                'status': False,
                'message': 'Invalid credentials'
            }
        existing = Users.query.filter_by(email=email).first()
        if existing:
            return {
                'status': 'fail',
                'message': 'User Already Exists'
            }
        else:
            hashed_password = bcrypt.hashpw(
                password.encode("utf-8"),
                bcrypt.gensalt()
            )
            user = Users(name=name, email=email, password=hashed_password, role=role)
            db.session.add(user)
            db.session.commit()
            return {
                'status': True,
                'message': 'User Created'
            }
