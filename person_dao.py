from database_setup import Base, Person
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import os

app = Flask(__name__)

engine = create_engine('sqlite:///personen.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def getAllPersonen():
    return session.query(Person).all()


def getPerson(aName):
    return session.query(Person).filter_by(name=aName).all()


def createPerson(aVorname, aNachname):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    person = Person(vorname=aVorname, name=aNachname)
    session.add(person)
    session.commit()
    print(person.id)
