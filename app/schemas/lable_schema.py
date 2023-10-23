from pydantic import BaseModel, Field


class CreateLable(BaseModel):
    name: str = Field(..., title="标签名称", min_length=1, max_length=15)
    color: str = Field(..., title="标签颜色", min_length=1, max_length=15)

