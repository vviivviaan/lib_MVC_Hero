class MemoryDatabase:
    def __init__(self):
        self._tables = {}
        self._id_counter = {}

    def _get_table(self, table_name):
        if table_name not in self._tables:
            self._tables[table_name] = []
            self._id_counter[table_name] = 1
        return self._tables[table_name]

    def insert(self, table_name: str, data: dict):
        table = self._get_table(table_name)
        data['id'] = self._id_counter[table_name]
        self._id_counter[table_name] += 1
        table.append(data)
        return data

    def select_all(self, table_name: str):
        return self._get_table(table_name)

    def select_by_id(self, table_name: str, record_id: int):
        table = self._get_table(table_name)
        return next((item for item in table if item['id'] == record_id), None)

    def delete(self, table_name: str, record_id: int):
        table = self._get_table(table_name)
        for item in table:
            if item['id'] == record_id:
                table.remove(item)
                return True
        return False
