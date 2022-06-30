def provinceEntity(item) -> dict:
    return {
        "province": item["province"],
        "district": [
            {
                "district": item["district"],
                "subdistrict": {
                    "subdistrict": item["district"][0]["subdistrict"][0]["subdistrict"]
                },
                "zip_code": {
                    "zip_code": item["district"][0]["subdistrict"][0]["zip_code"]
                }
            }
        ]
    }

def provinceallEntity(item) -> dict:
    return {
        "province": item["province"]
    }

def provincesEntity(entity) -> list:
    return [provinceallEntity(item) for item in entity]

def provinceslayerEntity(item,dis) -> dict:
    return {
        "district": item[dis]
    }