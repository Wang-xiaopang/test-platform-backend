import time
from xmindparser import xmind_to_dict
import copy
import os
from models.base_models.time_model import TimeModel

class XmindModel(TimeModel):

    async def upload_file(self, file):
        file1 = await file.read()
        filename = file.filename
        file_type = filename.split('.')[-1]
        if file_type == 'xmind':
            times_ = self.get_chinese_time()
            path = f'testfile/{times_}/{filename}'
            if not os.path.exists(f'testfile/{times_}'):
                os.makedirs(f'testfile/{times_}')
            with open(path, 'wb') as f:
                f.write(file1)

            return path

    def parser_file(self, path):
        data = {'data': []}
        xmind_dict = xmind_to_dict(path)
        test_demand = xmind_dict[0].get('topic')
        title = test_demand.get('title')
        title_list = title.split('\r\n')
        test_module_title = test_demand.get('topics')

        if len(title_list) != 1:
            data = {
                'demand_name': title_list[0],
                'demand_url': title_list[1],
                'data': []
            }

        case_data = {
            'module_name': '',
            'cases': []
        }
        try:
            for module in test_module_title:
                case_data.update({'module_name': module['title']})
                for case_name in module['topics']:
                    for case_steps in case_name['topics']:
                        steps_list = case_steps['title'].replace('\r', '\n').split('\n')
                        makers_list = case_steps.get('makers')
                        case_grade = None
                        step_tag = None
                        try:
                            for makers in makers_list:
                                if 'priority' in makers:
                                    if makers == 'priority-1':
                                        case_grade = 0
                                    elif makers == 'priority-2':
                                        case_grade = 1
                                    else:
                                        case_grade = 2
                                else:
                                    step_tag = makers
                        except TypeError as e:
                            logger.warning('优先级格式有误', e)

                        case_except = case_steps['topics'][0]
                        case_data['cases'].append({'case_name': case_name['title'],
                                                   'case_steps': steps_list,
                                                   'except': case_except['title'],
                                                   'case_grade': case_grade,
                                                   'step_tag': step_tag,
                                                   })
                tmp = copy.deepcopy(case_data)
                data['data'].append(tmp)
        except Exception as e:
            pass
        return data
