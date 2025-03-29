from flask import jsonify, request
from api.models.user import UserModel

class UserController:
    @staticmethod
    def get_users():
        """
        Obtener la lista de usuarios
        ---
        tags:
          - Usuarios
        responses:
          200:
            description: Lista de usuarios obtenida correctamente
        """
        users = UserModel.get_all_users()
        return jsonify(users), 200

    @staticmethod
    def create_user():
        """
        Crear un nuevo usuario
        ---
        tags:
          - Usuarios
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
          201:
            description: Usuario creado exitosamente
          400:
            description: Error en la solicitud
        """
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"message": "Username y password son requeridos"}), 400

        result = UserModel.create_user(username, password)
        
        if "error" in result:
            return jsonify(result), 400
        return jsonify(result), 201
