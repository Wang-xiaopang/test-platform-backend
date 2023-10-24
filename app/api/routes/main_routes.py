from api.routes.project_routes import project_router
from api.routes.iteration_routes import iteration_router
from api.routes.demand_routes import demand_router
from api.routes.module_routes import module_router
from api.routes.label_routes import label_router
from api.routes.case_routes import case_router
from api.routes.testcase_routes import testcase_router
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY



def all_routes():
    return [
        project_router,
        iteration_router,
        demand_router,
        module_router,
        label_router,
        case_router,
        testcase_router,
    ]


async def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
): 
    error_message = jsonable_encoder(exc.errors())[0]
    print(error_message)
    data = {
        'code':400,
        'msg':f'{error_message.get("loc")[0]}里的参数：{error_message.get("loc")[-1]}有问题：{error_message.get("msg")}',
        'data':{}
    }
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"data": data},
    )
