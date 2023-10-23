from fastapi import APIRouter
from schemas.case_schema import CreateCases, EditCase
from models.process_models.case_model import CaseModel

case_router = APIRouter()


@case_router.post("/case")
async def created_project(cr: CreateCases):
    cursor = CaseModel().create_cases(cr.project_id,cr.datas,cr.iteration_id)
    if cursor:
        data = {
            "code": 0,
            "msg": f"从项目{cr.project_id}创建用例成功",
            "data": {},
        }
    else:
        data = {"code": 1, "msg": f"从项目{cr.project_id}创建用例失败", "data": {}}
    return data


@case_router.get("/case/{project_id}")
async def get_projects(project_id: str):
    project_model = CaseModel()
    cursor = project_model.get_project_case(project_id)
    if cursor:
        datas = [{i.get("name"): str(i.get("_id"))} for i in cursor]
        data = {"code": 0, "msg": "查询成功", "data": datas}
    else:
        data = {"code": 1, "msg": "无数据", "data": {}}
    return data


@case_router.put("/case")
async def get_projects(cr: EditCase):
    cursor = CaseModel().edit_case(cr.case_id, cr.change_data)
    if cursor:
        data = {
            "code": 0,
            "msg": f"变更该用例数据{cr.change_data}成功",
            "data": {"case_id": str(cr.case_id)},
        }
    else:
        data = {"code": 1, "msg": f"变更该用例数据失败", "data": {}}
    return data
