from models.project_model import ProjectModel


class ModuleModel(ProjectModel):
    def __init__(self):
        super().__init__()
        self.module_col = "module"

    def create_module(self, name, project_id):
        """创建模块

        Args:
            name(str) 迭代名称
            project_id (str):  项目 id

        """
        # 检查是否有该项目
        check_project = self.check_project(project_id)
        if check_project:
            self.insert_data(
                self.module_col,
                {
                    "project_id": check_project,
                    "name": name,
                    "created_at": self.get_now_timestamp(),
                    "status": 0,
                },
            )

    def check_module(self, module_id):
        """检查模块是否存在

        Args:
            module_id ( str):  模块id

        Returns:
            cursor:  返回是否存在的 mongo 数据
        """
        object_str = self.str_to_object(module_id)
        if object_str:
            return self.find_data(self.module_col, {"_id": object_str})
        else:
            return

    def check_module_name(self, module_name):
        """检查模块名称是否存在

        Args:
            module_name ( str):  模块名称

        Returns:
            cursor:  返回是否存在的 mongo 数据
        """
        return self.find_data(self.module_col, {"name": module_name})

    def get_project_module(self, project_id):
        # 检查是否有该模块
        check_project = self.check_project(project_id)
        if check_project:
            return self.find_datas(self.module_col, {"project_id": check_project})
        else:
            return
