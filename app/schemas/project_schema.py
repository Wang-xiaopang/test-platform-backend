from pydantic import BaseModel, Field,ValidationError


class CreateProject(BaseModel):

    name: str = Field(..., title="项目名称", min_length=1, max_length=15)

