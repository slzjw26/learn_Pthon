import MySQLdb


host = '127.0.0.1'
port = 3306
user = 'wsgi'
password = 'wsgi'
db = 'wsgi'
charset = 'utf8'

conn = MySQLdb.connect(host=host, port=port,
                       user=user, password=password,
                       database=db, charset=charset)
cursor = conn.cursor()


def mod(cls):
    defined_fields = []
    for k, v in cls.__dict__.items():
        if isinstance(v, Field):
            defined_fields.append(k)
    cls.defined_fields = defined_fields
    return cls


class Field: ...


class CharField(Field):

    def __init__(self, max_length):
        self.max_length = max_length

    def validate(self, model, name):
        value = getattr(model, name, None)
        if value is None:
            raise ValueError('%s not exists' % name)
        if not isinstance(value, str):
            raise ValueError('%s is not a str' % name)
        if len(value) > self.max_length:
            raise ValueError('%s is too long' % name)


class IntegerField(Field):

    def __init__(self, default):
        self.default = default

    def validate(self, model, name):
        value = getattr(model, name, None)
        if value is None:
            setattr(model, name, self.default)
            value = self.default
        if not isinstance(value, int):
            raise ValueError('%s is not a int' % value)


class Model:

    def __init__(self, *junk, **kargs):
        for k, v in kargs.items():
            self.__dict__[k] = v

    def save(self):
        self.validate()
        if getattr(self, 'pk', None) is None:
            self.insert()
        else:
            self.update()

    def insert(self):
        sql = 'insert into %s (name, age) values(%%s, %%s)' % (self.tb_name)
        data = (self.name, self.age)
        cursor.execute(sql, data)
        conn.commit()
        self.pk = cursor.lastrowid

    def update(self):
        sql = 'update %s set name=%%s,age=%%s where id=%%s' % self.tb_name
        data = (self.name, self.age, self.pk)
        cursor.execute(sql, data)
        conn.commit()

    def validate(self):
        cls = self.__class__
        for field_name in cls.defined_fields:
            field_item = getattr(cls, field_name)
            field_item.validate(self, field_name)

    def delete(self):
        sql = 'delete from %s where id=%%s' % self.tb_name
        data = (self.pk,)
        cursor.execute(sql, data)
        conn.commit()

    @classmethod
    def search(cls, name=None, age=None):
        sql = 'select * from %s' % cls.tb_name
        data = []
        condition = []
        if name is not None:
            condition.append('name=%s')
            data.append(name)
        if age is not None:
            condition.append('age=%s')
            data.append(age)
        if condition:
            sql += ' where %s' % ' and '.join(condition)
        cursor.execute(sql, data)
        for id, name, age in cursor.fetchall():
            x = cls(name=name, age=age)
            x.pk = id
            yield x


@mod
class Student(Model):
    tb_name = 'student'
    name = CharField(max_length=16)
    age = IntegerField(default=0)

    def __str__(self):
        return '<Student name=%s age=%s>' % (self.name, self.age)

    def __repr__(self):
        return self.__str__()


class School:
    ...
    ...


if __name__ == '__main__':
    s1 = Student(name='Alice', age=18)
    s1.save()
