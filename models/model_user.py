from typing import List
from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    Id: str
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    name: str
    password: str