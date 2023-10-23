from api.routes.project_routes import project_router
from api.routes.iteration_routes import iteration_router
from api.routes.demand_routes import demand_router
from api.routes.module_routes import module_router
from api.routes.label_routes import label_router
from api.routes.case_routes import case_router

def all_routes():
    return [project_router,iteration_router,demand_router,module_router,label_router,case_router]