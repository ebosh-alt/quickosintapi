from collections import namedtuple

from .SQLite import Sqlite3_Database


class User:
    def __init__(self, id, **kwargs):
        self.id: int = id
        if len(kwargs):
            self.name: str | None = kwargs.get('name')
            self.password: str | None = kwargs.get('password')
            self.data_query: str | None = kwargs.get('data_query')
            self.type_query: str | None = kwargs.get('type_query')

        else:
            self.name: str | None = None
            self.password: str | None = None
            self.data_query: str | None = None
            self.type_query: str | None = None

    def __iter__(self):
        dict_class = self.__dict__
        Result = namedtuple("Result", ["name", "value"])
        for attr in dict_class:
            if not attr.startswith("__"):
                if attr != "flag":
                    yield Result(attr, dict_class[attr])
                else:
                    yield Result(attr, dict_class[attr].value)


class Users(Sqlite3_Database):
    def __init__(self, db_file_name, table_name, *args) -> None:
        Sqlite3_Database.__init__(self, db_file_name, table_name, *args)
        # self.len = len(self.get_keys())

    def add(self, obj: User) -> None:
        self.add_row(obj)
        # self.len += 1

    def __len__(self):
        return len(self.get_keys())

    def __delitem__(self, key):
        self.del_instance(key)
        # self.len -= 1

    def __iter__(self) -> User:
        keys = self.get_keys()
        for id in keys:
            user = self.get(id)
            yield user

    def get_id_by_name(self, name: str) -> User | bool:
        for user in self:
            if user.name == name:
                return user.id
        return False

    def get(self, id: int) -> User | bool:
        if id in self:
            obj_tuple = self.get_elem_sqllite3(id)
            obj = User(id=obj_tuple[0],
                       name=obj_tuple[1],
                       password=obj_tuple[2],
                       data_query=obj_tuple[3],
                       type_query=obj_tuple[4],
                       )
            return obj
        return False
