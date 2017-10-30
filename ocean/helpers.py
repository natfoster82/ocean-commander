from json import loads, dumps, JSONDecodeError


class Database:
    def __init__(self, filename='db.json'):
        self.filename = filename

    def get(self, key):
        try:
            with open(self.filename, 'r') as f:
                db_data = loads(f.read())
                value = db_data.get(key)
        except FileNotFoundError:
            value = None
        return value

    def set(self, key, value):
        with open(self.filename, 'w+') as f:
            try:
                db_data = loads(f.read())
            except JSONDecodeError:
                db_data = {}
            db_data[key] = value
            f.seek(0)
            f.write(dumps(db_data))
            f.truncate()


db = Database()



