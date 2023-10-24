from fastapi import APIRouter, UploadFile, File
from models.base_models.xmind_model import XmindModel

testcase_router = APIRouter()


@testcase_router.post("/xmind/upload")
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

@testcase_router.get("/xmind/parser/{filepath:path}")
def parser_xmind(filepath:str):
    xmind_model = XmindModel().parser_file(filepath)
    return xmind_model

@testcase_router.get("/xmind/del_file/{filepath:path}")
def del_file(filepath:str):
    # filepath = filepath.split('/')[:1]
    # filepath = ''.join(filepath)
    xmind_model = XmindModel().del_xmind(filepath)
    if xmind_model:
        return {"code":0,
                "msg":"删除成功",
                "data":{}}
    else:
        return {"code":1,
                "msg":"删除失败",
                "data":{}}