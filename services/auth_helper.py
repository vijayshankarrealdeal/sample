from typing import Optional
import jwt
import utils
import datetime
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException
from database_connect import dbs
from db.db_user_table import db_user_table
from passlib.context import CryptContext
from models.user_model import UserLogin, UserRegister
from op_logging import logging

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Auth:
    @staticmethod
    def encode_token(user_data):
        payload = {
            "exp": datetime.datetime.now() + datetime.timedelta(days=12),
            "sub": user_data.id,
        }
        try:
            token = jwt.encode(payload, "XYZ", algorithm="HS256")
            return {"token": token}
        except Exception as e:
            logging.debug(f"Error in encoding token: {e}")
            raise HTTPException(status_code=400, detail="Unkonwn error")

    async def register(self, user_data: UserRegister):
        user_data.password = pwd_context.hash(user_data.password)
        query = db_user_table.insert().values(**user_data.model_dump())
        try:
            user_id = await dbs.execute(query)
        except HTTPException as e:
            raise HTTPException(status_code=400, detail="Unkonwn error")
        user_data = await dbs.fetch_one(
            db_user_table.select().where(db_user_table.c.id == user_id)
        )
        return self.encode_token(user_data)

    async def login(self, user_data: UserLogin):
        user_data.password = pwd_context.hash(user_data.password)
        query = db_user_table.select().where(db_user_table.c.email == user_data.email)
        user_id = await dbs.execute(query)
        if not user_id:
            raise HTTPException(status_code=400, detail="Invalid email or password")
        user_db_data = await dbs.fetch_one(
            db_user_table.select().where(db_user_table.c.id == user_id)
        )
        if user_db_data.password != user_data.password:
            raise HTTPException(status_code=400, detail="Invalid email or password")
        return self.encode_token(user_db_data)


class CustomHTTPBearer(HTTPBearer):
    async def __call__(self, request) -> Optional[HTTPAuthorizationCredentials]:
        res = await super().__call__(request)
        try:
            payload = jwt.decode(res.credentials, "XYZ", algorithms=["HS256"])
            user_data = await dbs.fetch_one(
                db_user_table.select().where(db_user_table.c.id == payload["sub"])
            )
            if not user_data:
                raise HTTPException(401, "Invalid token")
            request.state.user = user_data
            return request
        except jwt.ExpiredSignatureError:
            raise HTTPException(401, "Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(401, "Invalid token")


oauth2_scheme = CustomHTTPBearer()


def is_admin(request):
    if request.state.user["user_type"] == "ADMIN":
        return True
    raise HTTPException(401, "You are not authorized.")
