from flask import Blueprint
from api.controllers.auth_controller import AuthController

auth_blueprint = Blueprint('auth', __name__)

auth_blueprint.route('/login', methods=['POST'])(AuthController.login)
