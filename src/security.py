from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    '''
    Function that gets called on /auth endpoint.

    :param username: User's username (str)
    :param password: User's password (str)
    :return: A user if the authentication was succesful, None if not
    '''
    user = UserModel.find_by_name(username)

    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    '''
    Function that gets called when a user already authenticatedm and Clask-JWT
    verified their authorization header is correct
    :param payload: A dict containing the identity key (user.id)
    :return: A UserModel object, None if not found
    '''
    user_id = payload.get('identity')
    return UserModel.find_by_id(user_id)