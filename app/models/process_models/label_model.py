from models.base_models.mongo_model import MongoModel
from models.base_models.time_model import TimeModel


class LabelModel(MongoModel,TimeModel):
    def __init__(self):
        super().__init__()
        self.label_col = "label"
        self.db[self.label_col].create_index([('name',1)],unique = True)

    def create_label(self, name, color):
        """创建迭代

        Args:
            name(str) 标签
            color (str):  颜色
        """
        # 检查是否有该项目

        return self.insert_data(
            self.label_col,
            {
                "name": name,
                "color": color,
                "created_at": self.get_now_timestamp(),
            },
        )

    def get_labels(self):
        # 获取所有标签

        return self.find_datas(self.label_col, {})
