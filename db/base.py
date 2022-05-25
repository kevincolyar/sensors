from datetime import datetime

class Base():
    def __init__(self, db, table_name):
        self.db = db
        self.table_name = table_name

    def all(self):
        return self.db.select("SELECT * FROM {0}".format(self.table_name))

    def destroy_all(self):
        return self.db.execute("DELETE FROM {0}".format(self.table_name))

    def select(self, sql):
        return self.db.select(sql)

    def insert(self, state):
        sanitized = {k: self._map_value(v) for k, v in state.items()}

        sql = "INSERT INTO {0} ({1}) VALUES ({2})".format(
            self.table_name,
            ', '.join(sanitized.keys()),
            ', '.join(sanitized.values()),
        )

        self.db.execute(sql)

    def count(self):
        return int(self.db.select("SELECT COUNT(*) as count FROM {0}".format(self.table_name))[0]['count'])

    def _map_value(self, v):
        if isinstance(v, datetime):
            return "'{0}'".format(
                v.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  # truncate the last 3 digits from datetime
            )
        elif isinstance(v, str):
            return "'{0}'".format(str(v))

        return str(v)
