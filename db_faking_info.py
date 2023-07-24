import sqlite3
import factory


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class UserFactory(factory.Factory):
    class Meta:
        model = User
    name = factory.Faker('name')
    age = factory.Faker('random_int', min=18, max=60)


conn = sqlite3.connect('./foo.db')
conn.isolation_level = None
cursor = conn.cursor()


cursor.execute('CREATE TABLE IF NOT EXISTS users ( \
                    id INTEGER PRIMARY KEY,        \
                    name TEXT NOT NULL,            \
                    age INTEGER)')


for _ in range(100):
    user = UserFactory()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (user.name, user.age))

conn.commit()
conn.close()
