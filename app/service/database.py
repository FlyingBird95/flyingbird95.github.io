from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()

db = SQLAlchemy()


def config_db(app):
    db.init_app(app)


class BaseModel(object):
    id = Column(Integer, primary_key=True, autoincrement=True)

    @classmethod
    def from_id(cls, id):
        return cls.query.filter(id=id).one()

    def __repr__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.id)
