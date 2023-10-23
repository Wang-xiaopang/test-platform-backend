from fastapi import APIRouter
from schemas.iteration_schema import CreateIteration, EditIteraion
from models.process_models.iteration_model import IterationModel
import pymongo

iteration_router = APIRouter()


@iteration_router.post("/iteration")
async def created_project(cr: CreateIteration):
    try:
        cursor = IterationModel().create_iteration(
            cr.name, cr.project_id, cr.start_time, cr.end_time
        )
        if cursor:
            data = {
                "code": 0,
                "msg": f"创建{cr.name}迭代成功",
                "data": {"iteration_id": str(cursor.inserted_id)},
            }
        else:
            data = {"code": 1, "msg": f"创建{cr.name}迭代失败", "data": {}}
    except pymongo.errors.DuplicateKeyError:
        data = {"code": 1, "msg": f"项目已存在该迭代,请勿重复创建", "data": {}}
    return data


@iteration_router.get("/iteration/{project_id}")
async def get_projects(project_id: str):
    project_model = IterationModel()
    cursor = project_model.get_project_iteration(project_id)
    if cursor:
        datas = [{i.get("name"): str(i.get("_id"))} for i in cursor]
        data = {"code": 0, "msg": "查询成功", "data": datas}
    else:
        data = {"code": 1, "msg": "无数据", "data": {}}
    return data


@iteration_router.put("/iteration")
async def get_projects(cr: EditIteraion):
    cursor = IterationModel().edit_iteration(cr.iteration_id, cr.status)
    if cursor:
        data = {
            "code": 0,
            "msg": f"变更该迭代状态为{cr.status}成功",
            "data": {"iteration_id": str(cr.iteration_id)},
        }
    else:
        data = {"code": 1, "msg": f"变更该迭代状态失败", "data": {}}
    return data
