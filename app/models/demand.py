from models.iteration_model import IterationModel


class DemandModel(IterationModel):
    def __init__(self):
        super().__init__()
        self.demand_col = "demand"

    def create_demand(self, name, iteration_id, start_time, end_time):
        """创建迭代

        Args:
            name(str) 迭代名称
            project_id (str):  项目 id
            start_time (int):  时间戳
            end_time (int):  时间戳
        """
        # 检查是否有该项目
        check_iteration = self.check_iteration(iteration_id)
        if check_iteration:
            self.insert_data(
                self.demand_col,
                {
                    "iteration_id": check_iteration,
                    "name": name,
                    "start_time": start_time,
                    "end_time": end_time,
                    "created_at": self.get_now_timestamp(),
                    "status": 0,
                },
            )

    def check_demand(self, demand_id):
        """检查迭代是否存在

        Args:
            demand_id ( str):  迭代id

        Returns:
            cursor:  返回是否存在的 mongo 数据
        """
        object_str = self.str_to_object(demand_id)
        if object_str:
            return self.find_data(self.demand_col, {"_id": object_str})
        else:
            return

    def edit_demand(self, demand_id, status):
        # 判断迭代是否存在
        check_demand = self.check_demand(demand_id)
        if check_demand:
            self.update_data(
                self.demand_col,
                {"_id": check_demand.get("_id")},
                {"status": status},
            )

    def get_iteration_demand(self, iteration_id):
        # 检查是否有该迭代
        check_iteration = self.check_iteration(iteration_id)
        if check_iteration:
            return self.find_datas(self.demand_col, {"iteration_id": iteration_id})
        else:
            return
