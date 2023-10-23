from pydantic import BaseModel, Field


class CreateModule(BaseModel):
    name: str = Field(..., title="需求名称", min_length=1, max_length=15)
    project_id: str = Field(..., title="项目id", min_length=24, max_length=24)

