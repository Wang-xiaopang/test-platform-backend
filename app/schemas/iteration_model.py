from pydantic import BaseModel, Field


class CreateIteration(BaseModel):
    name: str = Field(..., title="迭代名称", min_length=1, max_length=15)
    project_id: str = Field(..., title="项目id", min_length=24, max_length=24)
    start_time: int = Field(..., title="开始时间", min_length=10, max_length=10)
    end_time: int = Field(..., title="结束时间", min_length=10, max_length=10)


class EditIteraion(BaseModel):
    iteration_id : str = Field(..., title="迭代id", min_length=24, max_length=24)
    status : int = Field(..., title="迭代状态", min_length=0, max_length=2)