from fastapi import APIRouter

from schemas.project_schema import CreateProject
from models.project_model import ProjectModel

project_router = APIRouter()


@project_router.post("/project")
async def created_project(cr: CreateProject):
    project_model = ProjectModel()
    project_id = project_model.create_project(cr.name)
    if project_id:
        data = {
            "code": 0,
            "msg": f"创建{cr.name}项目成功",
            "data": {"project_id": str(project_id)},
        }
    else:
        data = {"code": 1, "msg": f"创建{cr.name}项目失败", "data": {}}
    return data


@project_router.get("/project")
async def get_projects():
    project_model = ProjectModel()
    cursor = project_model.get_projects()
    datas = [str(i.get("_id")) for i in cursor]
    return {"code": 0, "msg": f"查询成功", "data": {"projects": datas}}
