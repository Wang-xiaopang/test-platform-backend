from fastapi import FastAPI
from api.routes.main_routes import all_routes,request_validation_exception_handler
from fastapi.exceptions import RequestValidationError

import uvicorn

app = FastAPI()
app.add_exception_handler(RequestValidationError,request_validation_exception_handler)
for router in all_routes():
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
