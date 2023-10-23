from fastapi import FastAPI
from api.routes.project_routes import project_router
from api.routes.iteration_routes import iteration_router
from api.routes.demand_routes import demand_router
import uvicorn

app = FastAPI()

app.include_router(project_router)
app.include_router(iteration_router)
app.include_router(demand_router)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
