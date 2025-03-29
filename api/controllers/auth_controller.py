from flask import jsonify, request
from api.models.user import UserModel

class AuthController:
    @staticmethod
    def login():
        """
        Iniciar sesión en la API
        ---
        tags:
          - Autenticación
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                username:
                  type: string
                password:
                  type: string
        responses:
          200:
            description: Inicio de sesión exitoso
          401:
            description: Credenciales inválidas
        """
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = UserModel.get_user_by_username(username)

        if user and user['password'] == password:  # Comparación simple (mejor usar hash)
            return jsonify({"message": "Login exitoso"}), 200
        return jsonify({"message": "Credenciales inválidas"}), 401
