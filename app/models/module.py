from models.project_model import ProjectModel


class moduleModel(ProjectModel):
    def __init__(self):
        super().__init__()
        self.module_col = "module"

    def create_module(self, name, project_id, start_time, end_time):
        """创建迭代

        Args:
            name(str) 迭代名称
            project_id (str):  项目 id
            start_time (int):  时间戳
            end_time (int):  时间戳
        """
        # 检查是否有该项目
        check_project = self.check_project(project_id)
        if check_project:
            self.insert_data(
                self.module_col,
                {
                    "project_id": check_project,
                    "name": name,
                    "start_time": start_time,
                    "end_time": end_time,
                    "created_at": self.get_now_timestamp(),
                    "status": 0,
                },
            )

    def check_module(self, module_id):
        """检查迭代是否存在

        Args:
            module_id ( str):  迭代id

        Returns:
            cursor:  返回是否存在的 mongo 数据
        """
        object_str = self.str_to_object(module_id)
        if object_str:
            return self.find_data(self.module_col, {"_id": object_str})
        else:
            return

    def edit_module(self, module_id, status):
        # 判断迭代是否存在
        check_module = self.check_module(module_id)
        if check_module:
            self.update_data(
                self.module_col,
                {"_id": check_module.get("_id")},
                {"status": status},
            )

    def get_project_module(self, project_id):
        # 检查是否有该项目
        check_project = self.check_project(project_id)
        if check_project:
            return self.find_datas(self.module_col, {"project_id": check_project})
        else:
            return
