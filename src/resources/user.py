from models.user import UserModel

from flask_restful import Resource, reqparse

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank.")
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank.")

    def post(self):
        payload = UserRegister.parser.parse_args()

        if UserModel.find_by_name(payload.get('username')):
            return {
                'message': 'A user with that username already exists'
            }, 400

        user = UserModel(**payload)
        user.save_to_db()

        return {
            'message': 'User created succesfully'
        }, 201
