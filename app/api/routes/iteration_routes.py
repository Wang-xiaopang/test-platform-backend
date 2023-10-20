from fastapi import APIRouter
from schemas.iteration_model import CreateIteration, EditIteraion,GetIteraion
from models.iteration_model import IterationModel

iteration_router = APIRouter()


@iteration_router.post("/iteration")
async def created_project(cr: CreateIteration):
    project_model = IterationModel()
    project_model.create_iteration(cr.name, cr.project_id, cr.start_time, cr.end_time)
    return {"code": 0, "msg": f"创建{cr.name}项目成功", "data": {}}


@iteration_router.get("/iteration/{project_id}")
async def get_projects(project_id: str):
    project_model = IterationModel()
    cursor = project_model.get_project_iteration(project_id)
    datas = [str(i.get("_id")) for i in cursor]
    return {"code": 0, "msg": f"查询成功", "data": {"iterations": datas}}


@iteration_router.put("/iteration")
async def get_projects(cr: EditIteraion):
    project_model = IterationModel()
    project_model.edit_iteration(cr.iteration_id, cr.status)
    return {"code": 0, "msg": f"项目 id{cr.iteration_id}修改成功", "data": {}}
