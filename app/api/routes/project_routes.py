from fastapi import APIRouter
from schemas.project_schema import CreateProject
from models.process_models.project_model import ProjectModel
import pymongo

project_router = APIRouter()


@project_router.post("/project")
async def created_project(cr: CreateProject):
    try:
        print(cr)
        cursor = ProjectModel().create_project(cr.name)
        if cursor:
            data = {
                "code": 0,
                "msg": f"创建{cr.name}项目成功",
                "data": {"project_id": str(cursor.inserted_id)},
            }
        else:
            data = {"code": 1, "msg": f"创建{cr.name}项目失败", "data": {}}
    except pymongo.errors.DuplicateKeyError:
        data = {"code": 1, "msg": f"项目已存在,请勿重复创建", "data": {}}
    return data


@project_router.get("/project")
async def get_projects():
    project_model = ProjectModel()
    cursor = project_model.get_projects()
    datas = [{i.get('name'):str(i.get("_id"))} for i in cursor]
    return {"code": 0, "msg": f"查询成功", "data": datas}
