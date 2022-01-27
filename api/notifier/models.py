from enum import unique
from api import db_api
from sqlalchemy import Column, Integer, String

## Accounts to notify
class Contact(db_api.Model):

    __tablename__ = 'Contact'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, unique=True)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]
             
            setattr(self, property, value)

    def __repr__(self):
        return str(self.telegram_id)