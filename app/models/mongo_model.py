from pymongo import MongoClient
from dotenv import load_dotenv
import os


class MongoModel:
    def __init__(self):
        load_dotenv()
        mongo_url = os.getenv("MONGO_URL")
        mongo_db = os.getenv("MONGO_DB")
        cli = MongoClient(mongo_url)
        self.db = cli[mongo_db]

    def insert_data(self, col_name, data):
        """添加一条数据

        Args:
            data (dict): 需要加入的数据
        """

        self.db[col_name].insert_one(data)

    def insert_datas(self, col_name, datas):
        """添加多条数据

        Args:
            datas (list): 需要加入的多条数据
        """
        self.db[col_name].insert_many(datas)

    def update_data(self, col_name, tag_data, new_data):
        """更新一条数据

        Args:
            tag_data (dict): 标识到需要更新的数据
            new_data (dict): 更新的数据
        """
        self.db[col_name].update_one(tag_data, {"$set": new_data})

    def update_datas(self, col_name, tag_data, new_datas):
        """更新多条数据

        Args:
            tag_data (dict): 标识到需要更新的数据
            new_datas (dict): 更新的多条数据
        """
        self.db[col_name].update_one(tag_data, {"$set": new_datas})

    def find_data(self, col_name, tag_data, need_data={'_id':1}):
        """查找一条数据

        Args:
            tag_data (dict): 查找的标识数据
            need_data (dict): 需要留下的数据

        Returns:
            cursor: 返回的游标数据
        """
        cursor = self.db[col_name].find_one(tag_data, need_data)
        return cursor

    def find_datas(self, col_name, tag_datas, need_data={'_id':1}):
        """_summary_

        Args:
            tag_datas ( dict): 查找的标识数据
            need_data (ditc): 需要留下的数据

        Returns:
            cursor: 返回的游标数据
        """
        curosr = self.db[col_name].find(tag_datas, need_data)
        return curosr
