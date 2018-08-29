"""
BaseTest

Class should be the parent of all the subclasses (instead of inherit from TestCase)
It allows for instantiation of the database dynamically and makes sure it is a 
blank db each time
"""
from unittest import TestCase

from app import app
from db import db


def BaseTest(TestCase):

    def setUp(self):
        # Setup db 
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # gives a client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        # Makes sure that the db is erased
        with app.app_context():
            db.sesion.remove()
            db.drop_all()
        pass