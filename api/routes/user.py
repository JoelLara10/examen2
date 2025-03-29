from flask import Blueprint
from api.controllers.user_controller import UserController

users_blueprint = Blueprint('users', __name__)

users_blueprint.route('/', methods=['GET'])(UserController.get_users)
users_blueprint.route('/', methods=['POST'])(UserController.create_user)
