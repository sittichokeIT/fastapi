from dis import dis
from models.model_province import Province, District, Subdistrict, Project
from schemas.schema_province import provinceEntity, provincesEntity,provinceslayerEntity
from config.db import conn
from typing import List
from fastapi import APIRouter, Form, Body, Query

province = APIRouter()
Path_object = conn.Fastapi.layer1
Path_province = conn.Fastapi.province

@province.post('/saveProvice')
async def save_object(province: Province):
    Path_object.insert_one(province.dict())
    print(province)
    return {
        "message": dict(province)
    }

@province.post('/saveProject')
async def save_object(project: Project):
    Path_province.insert_one(dict(project))
    print(project)
    return {
        "message": dict(project)
    }

@province.post('/saveDistrict')
async def save_object(district: District):
    Path_province.insert_one(dict(district))
    print(province)
    return {
        "message": dict(district)
    }

@province.post('/saveSubdistrict')
async def save_object(subdistrict: Subdistrict):
    Path_province.insert_one(dict(subdistrict))
    print(province)
    return {
        "message": dict(subdistrict)
    }

@province.post('/saveProviceList')
async def save_province(province: Province ):
    Path_province.insert_one(dict(province))
    print(province.dict())
    return 0


# @province.get('/show/object_by_name')
# async def show_object_by_name():
#     check1 = Path_province.find_one({"title": "province"})# นนทบุรี
#     check = []
#     for i in range(len(check1["province"])):
#         print(i)
#         check[i] = []
    
#     print(check1)
    
#     # for i in range(len(check1["province"])):
#     #     check2 = Path_province.find_one({"province_":check1["province"][i-1]})# ไทรน้อย, บางบัวทอง
#     #     print(check2)

#     # for i in range(len(check2["district"])):
#     #     check3 = Path_province.find_one({"district_": check2["district"][i-1]})# ราษฎร์นิยม, บางรักใหญ่
#     #     print(check3)

#     # for i in range(len(check3["subdistrict"])):
#     #     check4 = Path_province.find_one({"subdistrict_":check3["subdistrict"][i-1]})
#     #     print(check4)
#     if check1 : 
#         return 0
#         # return {
#         #     "message": "User not found!"
#         # }
#     else : 
#         return {
#             "message": "User not found!"
#         }

@province.post('/test')
async def test():
    Path_object.insert_many([
    { "_id": "MongoDB", "ancestors": [ "Books", "Programming", "Databases" ], "parent": "Databases" },
    { "_id": "dbm", "ancestors": [ "Books", "Programming", "Databases" ], "parent": "Databases" },
    { "_id": "Databases", "ancestors": [ "Books", "Programming" ], "parent": "Programming" },
    { "_id": "Languages", "ancestors": [ "Books", "Programming" ], "parent": "Programming" },
    { "_id": "Programming", "ancestors": [ "Books" ], "parent": "Books" },
    { "_id": "Books", "ancestors": [ ], "parent": "" }
    ] )
    Path_object.find_one( { "_id": "MongoDB" } )["parent"]