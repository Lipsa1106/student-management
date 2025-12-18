import jwt
from flask_jwt_extended import create_access_token, get_jwt_identity, get_jwt


def create_token(user_id, name, email, role):
    return create_access_token(
        identity=str(user_id),   # ✅ MUST be string
        additional_claims={
            "role": role,
            "name": name,
            "email": email,
        }
    )

def verify_token(token):
    return {
        "user_id": get_jwt_identity(),
        "claims": get_jwt(),
    }
