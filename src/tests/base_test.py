"""
BaseTest

Class should be the parent of all the subclasses (instead of inherit from TestCase)
It allows for instantiation of the database dynamically and makes sure it is a 
blank db each time
"""
from unittest import TestCase
from sys import exc_info
from pdb import post_mortem
from functools import wraps
from traceback import print_exception

from app import app
from db import db


class BaseTest(TestCase):

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
            db.session.remove()
            db.drop_all()
        pass

    # Define a sexy decorator uwu
    def debug_on(*exceptions):
        if not exceptions:
            exceptions = (AssertionError,)
        def decorator(callback):
            @wraps(callback)
            def wrapper(*args, **kwargs):
                try:
                    return callback(*args, *kwargs)
                except exceptions:
                    info = exc_info()
                    print_exception(*info)
                    post_mortem(info[2])
            return wrapper
        return decorator
