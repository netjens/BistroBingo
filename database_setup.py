import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    vorname = Column(String(25), nullable=False)

    def serialize(self):
        return {'vorname': self.vorname, 'name': self.name}


engine = create_engine('sqlite:///personen.db')

Base.metadata.create_all(engine)
