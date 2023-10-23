from models.module_model import ModuleModel
from models.demand_model import DemandModel
from models.label_model import LabelModel


class CaseModel(ModuleModel, DemandModel, LabelModel):
    def __init__(self):
        super().__init__()
        self.case_col = "case"

    def case_data_deal(self, project_id, case_data, iteration_id=None):
        """处理测试用例数据

        Args:
            case_data (dict): 复杂的测试用力用例数据
            project_id (ObjcetId): 项目的逻辑id
            type_ (int, optional): 是否是模块. 默认0即第一条数据为需求，1为模块

        Returns:
            list: 处理后直接添加到数据的数据
        """
        # 判断是迭代还是需求
        demand_name = case_data.get("demand_name")
        if demand_name:
            # 拿到了就是需求，检查需求是否存在
            demand_data = self.check_demand_name(demand_name)
            if demand_data:
                # 需求存在直接拿到需求id
                demand_id = demand_data.get("_id")
                pass
            else:
                # 需求不存在，先新增拿到需求id
                self.create_demand(
                    demand_name,
                    iteration_id,case_data.get('demand_url')
                )
                # todo 查看是否能返回_id
            pass
        #读取二层数据   
        cases = case_data.get('data')
        for case in cases:
            module_name = case.get('module_name')
            second_cases = case.get('cases')



    def create_cases(self, project_id, case_data, iteration_id=None):
        """添加多条用例

        Args:
            project_id (ObjcetId): 项目的逻辑id
            case_data (dict(list(dict))): 测试用例数据
            iteration_id (ObjcetId, optional): 迭代id. Defaults to None.
        """
        # 检查是否有该项目
        check_project = self.check_project(project_id)
        if check_project:
            pass

    def check_case(self, case_id):
        """检查模块是否存在

        Args:
            case_id ( str):  模块id

        Returns:
            cursor:  返回是否存在的 mongo 数据
        """
        object_str = self.str_to_object(case_id)
        if object_str:
            return self.find_data(self.case_col, {"_id": object_str})
        else:
            return

    def get_project_case(self, project_id):
        # 检查是否有该模块
        check_project = self.check_project(project_id)
        if check_project:
            return self.find_datas(self.case_col, {"project_id": check_project})
        else:
            return
