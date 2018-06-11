import MySQLdb as db


host = 'localhost'
port = 3306
username = 'orm'
password = 'orm'
database = 'wsgi'
charset = 'utf8'


class Model:

    @classmethod
    def init_db(cls, host, port, user, password, database, charset):
        if getattr(cls, 'conn', None) is None:
            conn = db.connect(host=host, port=port,
                                    us er=username, password=password,
                                    database=database, charset=charset)
            cur = conn.cursor()
            Model.conn = conn
            Model.cur = cur

    @classmethod
    def save(cls, sql, data):
        cls.cur.execute(sql, data)
        cls.conn.commit()


class Student(Model):

    tb_name = 'student'

    def __init__(self, name=None, gender=None, age=None):
        self.name = name
        self.gender = gender
        self.age = age

    def save(self):
        sql = 'insert into %s (name, gender, age) values (%%s, %%s, %%s)' % self.tb_name
        data = (self.name, self.gender, self.age)
        Model.save(sql, data)


class Teacher(Model):

    tb_name = 'teacher'

    def __init__(self, name=None, gender=None, age=None, subject=None):
        self.name = name
        self.gender = gender
        self.age = age
        self.subject = subject

    def save(self):
        fmt = ('insert into %s (name, gender, age, subject) '
               'values (%%s, %%s, %%s, %%s)')
        sql = fmt % self.tb_name
        data = (self.name, self.gender, self.age, self.subject)
        Model.save(sql, data)


if __name__ == '__main__':

    # 初始化数据库环境
    Model.init_db(host, port, username, password, database, charset)

    # student = Student()
    # student.name = name
    # student.gender = gender
    # student.age = age
    student = Student(name='John Smith', gender='male', age=25)
    student.save()
    teacher1 = Teacher(name='Charlie', gender='male', age=35, subject='Python')
    teacher2 = Teacher(name='David', gender='male', age=55, subject='Django')
    teacher1.save()
    teacher2.save()
