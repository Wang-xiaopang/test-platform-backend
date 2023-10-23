from fastapi import APIRouter
from models.process_models.demand_model import DemandModel
from schemas.demand_schema import CreateDemand
import pymongo

demand_router = APIRouter()


@demand_router.post("/demand")
async def created_project(cr: CreateDemand):
    try:
        cursor = DemandModel().create_demand(cr.name, cr.iteration_id, cr.address)
        if cursor:
            data = {
                "code": 0,
                "msg": f"创建{cr.name}需求成功",
                "data": {"demand_id": str(cursor.inserted_id)},
            }
        else:
            data = {"code": 1, "msg": f"创建{cr.name}项目失败", "data": {}}
    except pymongo.errors.DuplicateKeyError:
        data = {"code": 1, "msg": f"项目已存在,请勿重复创建", "data": {}}
    return data


@demand_router.get("/demand/{iteration_id}")
async def get_projects(iteration_id):
    cursor = DemandModel().get_iteration_demand(iteration_id)
    if cursor:
        datas = [{i.get("name"): str(i.get("_id"))} for i in cursor]
        data = {"code": 0, "msg": "查询成功", "data": datas}
    else:
        data = {"code": 1, "msg": "无数据", "data": {}}
    return data
