from models.mongo_model import MongoModel


class LabelModel(MongoModel):
    def __init__(self):
        super().__init__()
        self.label_col = "label"

    def create_label(self, name, color):
        """创建迭代

        Args:
            name(str) 标签
            color (str):  颜色
        """
        # 检查是否有该项目

        self.insert_data(
            self.label_col,
            {
                "name": name,
                "color": color,
                "created_at": self.get_now_timestamp(),
            },
        )

    def check_label(self, label_id):
        """检查迭代是否存在

        Args:
            label_id ( str):  迭代id

        Returns:
            cursor:  返回是否存在的 mongo 数据
        """
        object_str = self.str_to_object(label_id)
        if object_str:
            return self.find_data(self.label_col, {"_id": object_str})
        else:
            return

    def edit_label(self, label_id, status):
        # 判断迭代是否存在
        check_label = self.check_label(label_id)
        if check_label:
            self.update_data(
                self.label_col,
                {"_id": check_label.get("_id")},
                {"status": status},
            )

    def get_project_label(self, project_id):
        # 检查是否有该项目
        check_project = self.check_project(project_id)
        if check_project:
            return self.find_datas(self.label_col, {"project_id": check_project})
        else:
            return
