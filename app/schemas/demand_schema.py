from pydantic import BaseModel, Field


class CreateDemand(BaseModel):
    name: str = Field(..., title="需求名称", min_length=1, max_length=30)
    iteration_id: str = Field(..., title="迭代id", min_length=24, max_length=24)
    address: str =  Field(..., title="需求地址")

