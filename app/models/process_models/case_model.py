from models.process_models.module_model import ModuleModel
from models.process_models.demand_model import DemandModel
from models.process_models.label_model import LabelModel


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
            else:
                # 需求不存在，先新增拿到需求id
                demand_id = self.create_demand(
                    demand_name, iteration_id, case_data.get("demand_url")
                )
        # 读取二层数据
        cases = case_data.get("data")
        result = []
        for case in cases:
            module_name = case.get("module_name")
            # 判断模块是否存在,不在就新增
            module_check = self.check_module_name(module_name)
            if module_check:
                module_id = module_check
            else:
                module_id = self.create_module(module_name, project_id)
            second_cases = case.get("cases")
            test_cases = []
            for test_case in second_cases:
                test_case["project_id"] = project_id
                test_case["module_id"] = module_id
                if demand_name:
                    test_case["iteration_id"] = iteration_id
                    test_case["demand_id"] = demand_id
                test_cases.append(test_case)
            result.extend(test_cases)
        return result

    def create_cases(self, data):
        # 处理数据
        result = self.case_data_deal(data)
        return self.insert_datas(self.case_col, result)

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

    def put_test_case(self, case_id, change_data):
        # 检查是否有该用例
        check_case = self.check_case(case_id)
        if check_case:
            return self.update_data(self.case_col, {"_id": case_id}, change_data)
        else:
            return

    def delete_case(self, case_id):
        # 检查是否有该用例
        check_case = self.check_case(case_id)
        if check_case:
            pass
