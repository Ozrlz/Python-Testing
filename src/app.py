from os import environ

from flask import Flask
from flask_restful import Api

from resources.item import Item, ItemList

app = Flask(__name__)

FLASK_PORT = environ.get('FLASK_PORT', 5000)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    from db import db

    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000, host='0.0.0.0', debug=True)
