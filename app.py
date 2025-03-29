from flask import Flask
from flasgger import Swagger
from api.routes.auth import auth_blueprint
from api.routes.user import users_blueprint

app = Flask(__name__)

# Configuración de Swagger
swagger = Swagger(app)

# Registrar rutas (Blueprints)
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(users_blueprint, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
