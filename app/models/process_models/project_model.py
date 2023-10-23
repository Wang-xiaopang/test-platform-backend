from models.base_models.mongo_model import MongoModel
from models.base_models.time_model import TimeModel
from models.base_models.objectid_model import ObjectidModel


class ProjectModel(TimeModel, MongoModel, ObjectidModel):
    def __init__(self):
        super().__init__()
        self.project_col = "project"
        self.db[self.project_col].create_index([('name',1)],unique = True)

    def create_project(self, project_name):
        """创建项目

        Args:
            project_name ( str): 项目名称
        """
        return self.insert_data(
            self.project_col,
            {"name": project_name, "created_at": self.get_now_timestamp()},
        )

    def get_projects(self):
        """查询所有的项目

        Returns:
             cursor:  可遍历的 cursor
        """
        return self.find_datas(self.project_col, {})

    def check_project(self, project_id):
        """检查项目是否存在

        Args:
            project_id ( str):  项目id

        Returns:
            cursor:  返回是否存在的 mongo 数据
        """
        # 判断能否转换成 object_id
        object_str = self.str_to_object(project_id)
        if object_str:
            return self.find_data(self.project_col, {"_id": object_str})
        else:
            return
