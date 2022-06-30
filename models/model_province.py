from typing import List, Union
from pydantic import BaseModel

class Subdistrict(BaseModel):
    subdistrict_: str
    zip_code: str

class District(BaseModel):
    # no: int
    # district: str
    district_: str
    subdistrict: List[str] = []

class Province(BaseModel):
    title: str
    province_: str
    district: List[str] = []

class Project(BaseModel):
    title: str
    province: List[str] = []
