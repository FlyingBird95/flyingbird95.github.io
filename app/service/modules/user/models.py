import hashlib
from datetime import datetime
from sqlalchemy import Column, String, DateTime

from app.service.database import db, BaseModel


class User(BaseModel, db.Model):
    __tablename__ = 'users'

    register_date = Column(DateTime, default=datetime.utcnow)
    email = Column(String(80), unique=True)
    password_hash = Column(String(80))

    @classmethod
    def from_email(cls, email):
        return cls.query.filter_by(email=email).one_or_none()

    def check_password(self, password_to_check):
        """Compares the given password with the one from the User.
        :rtype bool
        """
        return self.password_hash == self.encode_password(password_to_check)

    def set_password(self, new_password):
        self.password_hash = self.encode_password(new_password)

    @staticmethod
    def encode_password(password):
        m = hashlib.md5()
        m.update(password.encode('utf-8'))
        return m.hexdigest()
