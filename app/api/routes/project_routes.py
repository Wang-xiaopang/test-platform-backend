from fastapi import APIRouter
from app.schemas.project_schema import CreateProject
from models.project_model import ProjectModel

project_router = APIRouter()


@project_router.post("/project")
async def created_project(name: CreateProject):
    project_model = ProjectModel()
    project_model.create_project(name)
    return {"code": 0, "msg": f"创建{name}项目成功", "data": {}}
