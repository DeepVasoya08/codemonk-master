import os

import bcrypt
import jwt
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGO = os.getenv("JWT_ALGO")


def encrypt(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def decrypt(password: str, hashedPass: str):
    return bcrypt.checkpw(password.encode(), hashedPass.encode())


def generateToken(payload):
    try:
        return jwt.encode(payload, JWT_SECRET, JWT_ALGO)
    except Exception as e:
        return e


def verifyToken(data, request):
    try:
        user = jwt.decode(data, JWT_SECRET, JWT_ALGO)
        request.user = user
        return True
    except jwt.ExpiredSignatureError:
        request.user = False
        return "Token Expired"
    except Exception as e:
        request.user = False
        return False
