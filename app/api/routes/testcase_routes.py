from fastapi import APIRouter, UploadFile, File
from models.base_models.parser_model import ParserModel

testcase_router = APIRouter()


@testcase_router.post("/upload")
async def upload_file(file: UploadFile = File()):
    file_type = ParserModel().upload_file(file)
    if file_type == 'xmind':
        return {
            "code": 0,
            "msg": "上传文件成功",
        }
    else:
        return {
            "code": 1,
            "msg": "上传格式有误",
        }

@testcase_router.get("/parser")
async def parser_xmind():
    data = ParserModel().file_to_testcases()
    if