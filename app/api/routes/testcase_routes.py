from fastapi import APIRouter, UploadFile, File
from models.base_models.xmind_model import XmindModel

testcase_router = APIRouter()


@testcase_router.post("/upload")
async def upload_file(file: UploadFile = File()):
    xmind_model = XmindModel()
    path = await xmind_model.upload_file(file)
    if path:
        return {
            "code": 0,
            "msg": "上传文件成功",
            "data":{"path":path}
        }
    else:
        return {
            "code": 1,
            "msg": "上传格式有误",
            "data":{}
        }

@testcase_router.get("/parser/{filepath:path}")
def parser_xmind(filepath:str):
    xmind_model = XmindModel().parser_file(filepath)
    return xmind_model