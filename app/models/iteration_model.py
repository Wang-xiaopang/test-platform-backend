from project_model import ProjectModel


class IterationModel(ProjectModel):
    def __init__(self):
        super().__init__()
        self.iteration_col = "iteration"

    def create_iteration(self, name, project_id, start_time, end_time):
        """创建迭代

        Args:
            project_id (str):  项目 id
            start_time (int):  时间戳
            end_time (int):  时间戳
        """
        # 检查是否有该项目
        check_project = self.check_project(project_id)
        if check_project:
            self.insert_data(
                self.iteration_col,
                {
                    "project_id": check_project,
                    "name": name,
                    "start_time": start_time,
                    "end_time": end_time,
                    "created_at": self.get_now_timestamp(),
                    "status": 0,
                },
            )

    def check_iteration(self, iteration_id):
        """检查迭代是否存在

        Args:
            iteration_id ( str):  迭代id

        Returns:
            cursor:  返回是否存在的 mongo 数据
        """
        object_str = self.str_to_object(iteration_id)
        if object_str:
            return self.find_data(self.iteration_col, {"_id": object_str})
        else:
            return

    def edit_iteration(self, iteration_id, status):
        # 判断迭代是否存在
        check_iteration = self.check_iteration(iteration_id)
        if check_iteration:
            self.update_data(
                self.iteration_col,
                {"_id": check_iteration.get("_id")},
                {"status": status},
            )

    def get_project_iteration(self, project_id):
        # 检查是否有该项目
        check_project = self.check_project(project_id)
        if check_project:
            return self.find_datas(self.iteration_col, {"project_id": check_project})
        else:
            return
