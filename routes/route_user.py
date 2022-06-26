from asyncore import read
import shutil
from typing import List
from fastapi import APIRouter, UploadFile, File, Depends
from models.model_user import User, UserLogin
from config.db import conn
from schemas.schema_user import userEntity, usersEntity
from tabula import  read_pdf, convert_into

from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT

import base64
import bson
from bson.binary import Binary

user = APIRouter()
Path = conn.Fastapi.user
Path_file = conn.Fastapi.file


# , dependencies=[Depends(JWTBearer)]
@user.get('/')
async def find_all():
    # items = usersEntity(conn.Fastapi.user.find())
    # print(items[0]["name"])
    return {
        "result": usersEntity(Path.find())
    }

@user.get('/find-by-user/{name}')
async def find_by_user(name:str):
    # print(name)
    check = Path.find_one({"name": name})
    # print(check)
    if check :
        return userEntity(check)
    else : 
        return {
            "message": "User not found"
        }

@user.post('/')
async def create_user(user: User):
    # print(user.name)
    check = Path.find_one({"name": user.name})
    print(check)
    if check :
        return {
            "message": "User already exists"
        }
    else : 
        Path.insert_one(dict(user))
        return {
            "message": "Successfully created"
        }
        
@user.post('/login')
async def login(user: UserLogin):
    check = Path.find_one({"name": user.name,"password": user.password})
    print(check["email"])
    if check :
        return signJWT(check["email"])
    else :
        return {
            "error": "Wrong login details!"
        }
        
   
@user.post('/update/{id}')
async def update_user(id:str, user: User ):
    Path.update_one({"Id":id},{"$set":dict(user)})
    return {
        "Successfully update"
    } 
    
@user.post('/delete/{id}')
async def delete_user(id:str):
    Path.delete_one({"Id":id})
    return {
        "message": "Successfully deleted"
    }
    
@user.post('/UploadFile')
async def upload_file(file: UploadFile = File(...)): 
    with open("file/"+file.filename, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer) 
    # save to mongodb
    with open("file/"+file.filename, "rb") as buffer:
        # encoded = Binary(buffer.read())   
        encoded = base64.b64encode(buffer.read())
    
    data = read_pdf("./file/"+file.filename, pages="all")
    # print(data["รหสัลูกคา้  10010605"])
    
    # print(data)
    convert_into("./file/"+file.filename,"./filePDF/"+file.filename+".csv", pages="all",output_format="csv")
    Path_file.insert({"filename": file.filename, "file": encoded})
    return {"file_name": file.filename}
    
@user.post('/UploadFileList')
async def upload_fileList(file: List[UploadFile] = File(...)):  
    for f in file:
        with open("file/"+f.filename, 'wb') as buffer:
            shutil.copyfileobj(f.file, buffer) 
    return {"file_name": "good"}

@user.get('/downloadFilePDF/{name}')
async def download_filePDF(name: str):
    check = Path_file.find_one({"filename": name})
    file_64_decode = base64.b64decode(check["file"])
    file_result = open(check["filename"],"wb")
    file_result.write(file_64_decode)
    print(check["filename"])