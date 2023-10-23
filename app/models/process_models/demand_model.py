from models.process_models.iteration_model import IterationModel


class DemandModel(IterationModel):
    def __init__(self):
        super().__init__()
        self.demand_col = "demand"
        self.db[self.demand_col].create_index([('name',1),('iteration_id',1)],unique = True)

    def create_demand(self, name, iteration_id, address):
        """创建需求

        Args:
            name(str) 需求名称
            iteration_id (str):  迭代 id
            address (str):  需求地址
        """
        # 检查是否有该项目
        check_iteration = self.check_iteration(iteration_id)
        if check_iteration:
            return self.insert_data(
                self.demand_col,
                {
                    "iteration_id": check_iteration.get('_id'),
                    "name": name,
                    "address": address,
                    "created_at": self.get_now_timestamp(),
                },
            )

    def check_demand(self, demand_id):
        """检查需求是否存在

        Args:
            demand_id ( str):  需求id

        Returns:
            cursor:  返回是否存在的 mongo 数据
        """
        object_str = self.str_to_object(demand_id)
        if object_str:
            return self.find_data(self.demand_col, {"_id": object_str},{'_id':1})
        else:
            return

    def check_demand_name(self, demand_name):
        """检查需求名称是否存在

        Args:
            demand_name ( str):  需求名称

        Returns:
            cursor:  返回是否存在的 mongo 数据
        """
        return self.find_data(self.demand_col, {"name": demand_name})

    def get_iteration_demand(self, iteration_id):
        # 检查是否有该需求
        check_iteration = self.check_iteration(iteration_id)
        if check_iteration:
            return self.find_datas(self.demand_col, {"iteration_id": check_iteration.get('_id')})
        else:
            return
