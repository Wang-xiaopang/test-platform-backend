from fastapi import APIRouter
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from schemas.project_schema import CreateProject
from models.project_model import ProjectModel

project_router = APIRouter()


@project_router.post("/project")
async def created_project(name: CreateProject):
    project_model = ProjectModel()
    project_model.create_project(name)
    return {"code": 0, "msg": f"创建{name}项目成功", "data": {}}


@project_router.get("/project")
async def get_projects():
    project_model = ProjectModel()
    cursor = project_model.get_projects()
    return {"code": 0, "msg": f"查询成功", "data": {"projects": cursor}}

