from fastapi import APIRouter
from schemas.module_schema import CreateModule
from models.process_models.module_model import ModuleModel
import pymongo

module_router = APIRouter()


@module_router.post("/module")
async def created_project(cr: CreateModule):
    try:
        cursor = ModuleModel().create_module(cr.name,cr.project_id)
        if cursor:
            data = {
                "code": 0,
                "msg": f"创建{cr.name}模块成功",
                "data": {"module_id": str(cursor.inserted_id)},
            }
        else:
            data = {"code": 1, "msg": f"创建{cr.name}模块失败", "data": {}}
    except pymongo.errors.DuplicateKeyError:
        data = {"code": 1, "msg": f"项目已存在该模块,请勿重复创建", "data": {}}
    return data


@module_router.get("/module/{project_id}")
async def get_projects(project_id: str):
    cursor = ModuleModel().get_project_module(project_id)
    if cursor:
        datas = [{i.get("name"): str(i.get("_id"))} for i in cursor]
        data = {"code": 0, "msg": "查询成功", "data": datas}
    else:
        data = {"code": 1, "msg": "无数据", "data": {}}
    return data


