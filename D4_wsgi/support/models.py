import MySQLdb as db

DB_USER = 'wsgi'
DB_PASSWD = 'wsgi'
DB_DB = 'wsgi'
DB_HOST = 'localhost'
DB_PORT = 3306
DB_CHARSET = 'utf8'

db_conn = None
db_cursor = None


def db_connect():
    global db_conn, db_cursor
    db_conn = db.connect(host=DB_HOST, port=DB_PORT,
                         user=DB_USER, passwd=DB_PASSWD,
                         database=DB_DB, charset=DB_CHARSET)
    db_cursor = db_conn.cursor()


# connect to database
if db_conn is None:
    db_connect()


def mod(cls):
    cls.tb_name = cls.__name__.lower()
    attrs = cls.__dict__
    fields = [k for k, v in attrs.items() if isinstance(v, Field)]
    cls.fields = fields
    return cls


class Field:

    def validate(self, model, name):
        value = getattr(model, name, None)
        if value is None:
            raise AttributeError('field "%s" is not set' % name)
        return value


class CharField(Field):

    def __init__(self, max_length):
        self.max_length = max_length

    def validate(self, model, name):
        value = Field.validate(self, model, name)
        if not (isinstance(value, str) and len(value) <= self.max_length):
            raise AttributeError('invalid value of field "%s"' % name)


class IntegerField(Field):

    def __init__(self, default):
        self.default = default

    def validate(self, model, name):
        value = getattr(model, name, None)
        if value is None:
            value = self.default
        if not isinstance(value, int):
            raise AttributeError('invalid value of field "%s"' % name)


class Model:

    pk = None

    def __init__(self, *junk, **kargs):
        for k, v in kargs.items():
            if k not in self.fields:
                raise AttributeError('"%s" is not a defined field' % k)
            setattr(self, k, v)

    def validate(self):
        # raise an exception on validation failure
        for name in self.fields:
            defined_field = getattr(self.__class__, name)
            defined_field.validate(self, name)

    def save(self):
        self.validate()
        if getattr(self, 'pk', None) is None:
            self.insert()
        else:
            self.update()

    def insert(self):
        sql = 'insert into %s (%s) values(%s)' % (
                self.tb_name,
                ','.join(self.fields),
                ','.join(['%s' for i in range(len(self.fields))])
                )
        data = tuple(getattr(self, k) for k in self.fields)
        r = db_cursor.execute(sql, args=data)
        if r:
            pk = db_cursor.lastrowid
            self.pk = pk
            db_conn.commit()

    def update(self):
        sql = 'update %s set %s where id=%s' % (
                self.tb_name,
                ','.join(['%s=%%s' % k for k in self.fields]),
                self.pk
                )
        data = tuple(getattr(self, k) for k in self.fields)
        r = db_cursor.execute(sql, args=data)
        if r:
            db_conn.commit()

    def delete(self):
        sql = 'delete from %s where id=%s' % (
                self.tb_name,
                self.pk
                )
        r = db_cursor.execute(sql)
        if r:
            db_conn.commit()

    @classmethod
    def search(cls, *junk, **kargs):
        if not kargs:
            sql = 'select * from %s' % cls.tb_name
            r = db_cursor.execute(sql)
        else:
            items = list(kargs.items())
            keys = [k for k, v in items]
            data = tuple(v for k, v in items)
            sql = 'select * from %s where %s' % (
                    cls.tb_name,
                    ' and '.join(['%s=%%s' % k for k in keys]),
                    )
            r = db_cursor.execute(sql, args=data)

        if r:
            fields = cls.fields
            result = []
            for item in db_cursor.fetchall():
                pk = item[0]
                mod_instance = cls(**dict(zip(fields, item[1:])))
                mod_instance.pk = pk
                result.append(mod_instance)
            return result


@mod
class Student(Model):
    name = CharField(max_length=16)
    age = IntegerField(default=0)

    def __str__(self):
        return '<%s [%s, %s]>' % (self.__class__.__name__, self.name, self.age)

    def __repr__(self):
        return self.__str__()
