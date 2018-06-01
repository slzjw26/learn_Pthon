import pymysql
import time

dict = {'n': 'resume_name', 's': 'resume_sex', 'a': 'resume_age', 't': 'resume_telephone', 'e': 'resume_email',
        'ab': 'resume_ability', 'm': 'resume_mode', 'gt': 'resume_graduation_time', 'u': 'resume_university',
        'it': 'resume_interview_time'}
quanju = ''
time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def executeDatabase(sql, param=()):  # update,insert,delete
    conn=pymysql.connect(
    host='192.168.7.157',  #连接的数据库的IP
    port=3306,         #连接数据库的端口
    user='admin',       #连接数据库所使用的用户名
    passwd='123456',     #连接数据库用户的密码
    db='manage',          #连接的目标数据库名字
    charset="utf8"
    )
    cursor = conn.cursor()
    ret = cursor.execute(sql, param)
    conn.commit()
    cursor.close()
    conn.close()
    return ret


def findDatabase(sql, param=()):  # find
    retTuple = ()
    conn=pymysql.connect(
    host='192.168.7.157',  #连接的数据库的IP
    port=3306,         #连接数据库的端口
    user='admin',       #连接数据库所使用的用户名
    passwd='123456',     #连接数据库用户的密码
    db='manage',          #连接的目标数据库名字
    charset="utf8"
    )
    cursor = conn.cursor()
    cursor.execute(sql, param)
    retTuple = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return retTuple


def new(a):
    conn=pymysql.connect(
    host='192.168.7.157',  #连接的数据库的IP
    port=3306,         #连接数据库的端口
    user='admin',       #连接数据库所使用的用户名
    passwd='123456',     #连接数据库用户的密码
    db='manage',          #连接的目标数据库名字
    charset="utf8"
    )
    cur = conn.cursor()
    # 增加

    print('====简历录入====')
    name = input('姓名：')
    while 1:
        if name == '':
            name = input('姓名：')
        else:
            break
    sex = input('性别：')
    while 1:
        if sex == '男' or sex == '女':
            break
        else:
            sex = input('性别：')
    ability = input('技能方向：')
    graduation_time = input('毕业时间：')
    while 1:
        if graduation_time == '':
            graduation_time = input('毕业时间：')
        else:
            break
    university = input('毕业院校：')
    while 1:
        if university == '':
            university = input('毕业院校：')
        else:
            break
    telephone = input('电话号码：')
    while 1:
        if telephone == '':
            telephone = input('电话号码：')
        else:
            break
    email = input('邮箱：')
    mode = input('全职、兼职：')
    while 1:
        if mode == '':
            mode = input('全职、兼职：')
        else:
            break
    age = input('年龄')

    dem = cur.execute('''insert into resume
    (resume_name,resume_sex,resume_age,resume_telephone,resume_email,resume_ability,
    resume_graduation_time,resume_university,resume_mode,resume_operation_time,resume_creatorid
    ) 
    values
    ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}')'''
                      .format(name, sex, age, telephone, email, ability, graduation_time, university,
                              mode, time1, a))
    cur.close()  # 关闭游标
    conn.commit()  # 提交数据
    conn.close()


def query():  # 查询简历信息函数
    while 1:
        conn=pymysql.connect(
        host='192.168.7.157',  #连接的数据库的IP
        port=3306,         #连接数据库的端口
        user='admin',       #连接数据库所使用的用户名
        passwd='123456',     #连接数据库用户的密码
        db='manage',          #连接的目标数据库名字
        charset="utf8"
        )
        cur = conn.cursor()  # 定义游标
        print("----------------简历查询---------------")
        query1 = input("请输入查询方式（1.精确查询/2.关键字查询）：")
        if query1 == "1":
            precise = input("请输入正确的电话号码或者邮箱：")
            sql1 = cur.execute(
                "select * from resume where  resume_telephone='%s' or resume_email='%s'" % (precise, precise))
            if sql1 != 0:
                info = cur.fetchmany(sql1)
                for q, w, e, r, t, y, u, i, o, p, s, d, f, g in info:
                    print("resume_id:", q, "resume_name:", w, "resume_sex:", e, "resume_age:", r, "resume_telephone:", t,
                          "resume_email:", y,
                          "resume_ability", u, "resume_mode", i, "resume_graduation_time:", o, "resume_university:", p,
                          "resume_interview_time:", s,
                          "resume_creatorid", d, "resume_principalid:", f, "resume_operation_time", g)
                    break
            else:
                print("您要查询的不存在")
        elif query1 == "2":
            keyword = input("请输入需要查询的关键字：")
            a = '%' + keyword + '%'
            sql2 = cur.execute(
                "select * from resume where resume_id like '%s' or resume_name like '%s'or resume_sex like '%s' or "
                "resume_age like '%s' or resume_telephone like '%s' or resume_email like '%s' or resume_ability like '%s' "
                "or resume_mode like '%s' or resume_university like '%s'" % (a, a, a, a, a, a, a, a, a))
            if sql2 != 0:
                info = cur.fetchmany(sql2)
                for q, w, e, r, t, y, u, i, o, p, s, d, f, g in info:
                    print("resume_id:", q, "resume_name:", w, "resume_sex:", e, "resume_age:", r, "resume_telephone:", t,
                          "resume_email:", y,
                          "resume_ability", u, "resume_mode", i, "resume_graduation_time:", o, "resume_university:", p,
                          "resume_interview_time:", s,
                          "resume_creatorid", d, "resume_principalid:", f, "resume_operation_time", g)
                    break
            else:
                print("您要查询的信息不存在。")
        else:
            print("您要查询的方式错误。")
            return
        cur.close()  # 关闭游标
        conn.commit()  # 提交数据
        conn.close()


def update():
    conn=pymysql.connect(
    host='192.168.7.157',  #连接的数据库的IP
    port=3306,         #连接数据库的端口
    user='admin',       #连接数据库所使用的用户名
    passwd='123456',     #连接数据库用户的密码
    db='manage',          #连接的目标数据库名字
    charset="utf8"
    )
    cur = conn.cursor()  # 定义游标
    x = input('''请输入你想要修改的简历数据:
姓名:n, 性别:s, 年龄:a, 电话:t, 邮件:e, 能力:ab, 全职/兼职:m, 毕业学校:u, 毕业时间:gt, 面试时间:it\n''')
    while 1:
        if x in dict:
            y = input('请输入你想修改的简历的id:\n')
            list = getPrivileges(y)
            if list[0][0] != None:
                print("无法同时操作")
            else:
                setPrivileges(1)
                if x in ['gt', 'it']:
                    z = input('请输入你修改后的数据(xxxx-xx-xx):\n')
                else:
                    z = input('请输入你修改后的数据:\n')
                if x not in ['a', 'gt', 'it']:
                    sql = cur.execute("update resume set %s = '%s', resume_operation_time = '%s' where resume_id = %s"
                                      % (dict[x], z, time1, y))
                elif x == 'a':
                    sql = cur.execute("update resume set %s = %s, resume_operation_time = '%s' where resume_id = %s"
                                      % (dict[x], z, time1, y))
                else:
                    sql = cur.execute("update resume set %s = '%s', resume_operation_time = '%s' where resume_id = %s"
                                      % (dict[x], z, time1, y))
                setPrivileges(0)
                break
        else:
            x = input('指令错误,请重试:\n')
        cur.close()  # 关闭游标
        conn.commit()  # 提交数据
        conn.close()


def getPrivileges(id):
    sql = "select resume_principalid from resume where resume_id = %s"
    param = [id]
    list = findDatabase(sql, param)
    return list


def setPrivileges(id):
    if id == 1:
        sql = "update resume set resume_principalid= 1 where resume_id = %s "
        param = [id]
        executeDatabase(sql, param)
    else:
        sql = "update resume set resume_principalid=NULL where resume_id = %s"
        param = [id]
        executeDatabase(sql, param)


def resumeDelete():
    resumeID = input("输入要删除的ID：\n")
    list = getPrivileges(resumeID)
    print(list[0][0])
    if list[0][0] != None:
        print("无法同时操作")
    else:
        setPrivileges(1)
        sql = "delete from resume where resume_id=%s"
        param = ([resumeID],)
        executeDatabase(sql, param)
        setPrivileges(0)


def staffFunc():  # 员工操作函数
    while 1:
        flag = int(input("员工界面，1添加简历，2查询简历，3删除简历，4修改简历状态"))
        if 1 == flag:
            new(quanju)
            break
        elif 2 == flag:
            query()
            break
        elif 3 == flag:
            resumeDelete()
            break
        elif 4 == flag:
            update()
            break
        else:
            print("输入错误")


def login(job):  # 登录验证
    global quanju
    quanju = input("请输入用户id：\n")
    passwd = input("请输入密码:\n")
    sql = "select * from user where user_id=%s and user_password=%s and user_job=%s"
    param = (quanju, passwd, job)
    ret = executeDatabase(sql, param)
    return ret


def officerFunc():  # 主管操作函数

    flag = int(input("主管界面，1查看员工信息，2查看招聘信息\n"))
    if 1 == flag:
        sql = "select * from user"
    elif 2 == flag:
        sql = "select * from resume"
    else:
        print("查询错误")
        return
    result = findDatabase(sql)
    for data in result:
        print(data)


def main():
    while True:
        uType = int(input("选择登录方式：1专员，2主管,3退出\n"))
        if 1 == uType:
            ret = login("专员")
            if ret > 0:  # 专员通过验证
                staffFunc()
            else:
                print("密码错误")
        elif 2 == uType:
            ret = login("主管")
            if ret > 0:  # 主管通过验证
                officerFunc()
            else:
                print("密码错误")
        elif 3==uType:
            break
        else:
            print("请选择登录身份")


if __name__ == '__main__':
    main()
