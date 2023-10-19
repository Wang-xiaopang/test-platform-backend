from bson import objectid, errors


class ObjectidModel:
    def str_to_object(self,str):
        try:
            object_str = objectid.ObjectId(str)
            return object_str
        except errors.InvalidId:
            return
