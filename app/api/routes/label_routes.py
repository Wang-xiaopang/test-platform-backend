from fastapi import APIRouter
from schemas.lable_schema import CreateLable
from models.process_models.label_model import LabelModel
import pymongo

label_router = APIRouter()


@label_router.post("/label")
async def created_project(cr: CreateLable):
    try:
        cursor = LabelModel().create_label(cr.name,cr.color)
        if cursor:
            data = {
                "code": 0,
                "msg": f"创建{cr.name}标签成功",
                "data": {"label_id": str(cursor.inserted_id)},
            }
        else:
            data = {"code": 1, "msg": f"创建{cr.name}标签失败", "data": {}}
    except pymongo.errors.DuplicateKeyError:
        data = {"code": 1, "msg": f"已存在该标签,请勿重复创建", "data": {}}
    return data


@label_router.get("/label")
async def get_projects():
    cursor = LabelModel().get_labels()
    if cursor:
        datas = [{i.get("name"):i.get("color")} for i in cursor]
        data = {"code": 0, "msg": "查询成功", "data": datas}
    else:
        data = {"code": 1, "msg": "无数据", "data": {}}
    return data


