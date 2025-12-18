from extensions import db


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False,
        index=True
    )

    role = db.Column(db.String(50), nullable=False)

    password = db.Column(db.LargeBinary, nullable=False)
