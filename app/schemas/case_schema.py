from pydantic import BaseModel, Field


class CreateCases(BaseModel):
    project_id: str = Field(..., title="项目id", min_length=24, max_length=24)

    datas: dict = Field(..., title="用例数据")
    iteration_id: str = Field(None, title="迭代id", min_length=24, max_length=24)


class EditCase(BaseModel):
    case_id: str = Field(..., title="用例id", min_length=24, max_length=24)
    change_data: dict = Field(..., title="修改数据")
