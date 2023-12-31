from pydantic import BaseModel, Field


class CreateIteration(BaseModel):
    name: str = Field(..., title="迭代名称", min_length=1, max_length=15)
    project_id: str = Field(..., title="项目id", min_length=24, max_length=24)
    start_time: int = Field(..., title="开始时间", ge=1000000000, le=9999999999)
    end_time: int = Field(..., title="结束时间", ge=1000000000, le=9999999999)


class EditIteraion(BaseModel):
    iteration_id: str = Field(..., title="迭代id", min_length=24, max_length=24)
    status: int = Field(..., title="迭代状态", ge=0, le=2)
