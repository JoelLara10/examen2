import pymysql
from config import Config

def get_db_connection():
    """Conecta a la base de datos MySQL"""
    return pymysql.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

class UserModel:
    @staticmethod
    def get_all_users():
        """Obtiene todos los usuarios de la base de datos"""
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, username FROM users")
            users = cursor.fetchall()
        connection.close()
        return users

    @staticmethod
    def get_user_by_username(username):
        """Obtiene un usuario por su nombre"""
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, username, password FROM users WHERE username=%s", (username,))
            user = cursor.fetchone()
        connection.close()
        return user

    @staticmethod
    def create_user(username, password):
        """Crea un nuevo usuario en la base de datos"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            connection.commit()
            return {"message": "Usuario creado exitosamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            connection.close()
