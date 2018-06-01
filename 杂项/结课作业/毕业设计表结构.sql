/*========================公司员工薪水管理系统start========================*/
/*
    总薪水=基本薪水+奖金
    关系：
        1、employ.deptid = dept.deptid(某个员工属于某个部门)
        2、employ.stationid = station.stationid(某个员工在某个部门任职的岗位)
        3、salary.employid = employ.employid(某个员工的薪新)
*/
create table dept(
       deptid int, 
       deptname char(50)
);
alter table DEPT add constraint PK_DEPT primary key(DEPTID);
comment on table dept is '部门信息';
comment on column dept.deptid is '部门ID';
comment on column dept.deptname is '部门名称';

create table station(
       stationid int,
       stationname char(50)
);
alter table STATION add constraint PK_STATION primary key (STATIONID);
comment on table station is '岗位信息';
comment on column station.stationid is '岗位ID';
comment on column station.stationname is '岗位名称';

create table employ(
       employID int,
       ename char(50),
       sex char(50),
       age int,
       deptid int,
       stationid int
); 
alter table EMPLOY add constraint PK_EMPLOY primary key (EMPLOYID);
comment on table employ is '员工信息';
comment on column employ.employID is '员工ID';
comment on column employ.ename is '员工姓名';
comment on column employ.sex is '性别';
comment on column employ.age is '年龄';
comment on column employ.deptid is '部门ID';
comment on column employ.stationid is '岗位ID';

create table salary(
       salaryid int,
       employid int,
       basesalary int,
       bonussalary int
);
alter table SALARY add constraint PK_salary primary key (SALARYID);
comment on table salary is '员工薪水';
comment on column salary.salaryid is '薪水ID';
comment on column salary.employid is '员工ID';
comment on column salary.basesalary is '基本薪水';
comment on column salary.bonussalary is '奖金';
/*========================公司员工薪水管理系统end========================*/



/*========================个人简历管理系统start========================*/
/*
    关系：
        1、 companystation.companyid = company.companyid(某个人所在某个公司任职岗位)
        2、 companystation.personid = person.personid(某个人所在某个公司任职岗位)
        3、 experience.companystationid = companystation.companystationid(某个人所有任职公司的工作经历)
*/
create table person(
       personID int,
       ename char(50),
       sex char(50),
       age int
); 
alter table PERSON add constraint PK_PERSON primary key (PERSONID);
comment on table person is '个人信息';
comment on column person.personID is '人员ID';
comment on column person.ename is '名称';
comment on column person.sex is '性别';
comment on column person.age is '年龄';

create table company(
       companyid int,
       companyname char(50)
);
alter table COMPANY add constraint PK_COMPANY primary key (COMPANYID);
comment on table company is '工作单位';
comment on column company.companyid is '公司ID';
comment on column company.companyname is '公司名称';

create table companystation(
       companystationid int,
       companyid int,
       personid int,
       stationname char(50)
);
alter table COMPANYSTATION add constraint PK_COMPANYSTATION primary key (COMPANYSTATIONID);
comment on table companystation is '个人所在公司的岗位';
comment on column companystation.companystationid is '个人所在公司的岗位ID';
comment on column companystation.companyid is '公司ID';
comment on column companystation.personid is '个人ID';
comment on column companystation.stationname is '岗位名称';

create table experience(
       experienceid int,
       companystationid int,
       startdate date,
       enddate date,
       descsr char(1000),
       salary int
);
alter table EXPERIENCE add constraint PK_EXPERIENCE primary key (EXPERIENCEID);
comment on table experience is '个人工作经历';
comment on column experience.experienceid is '经历ID';
comment on column experience.companystationid is '个人所在公司的岗位ID';
comment on column experience.startdate is '工作起始日期';
comment on column experience.enddate is '工作结束日期';
comment on column experience.descsr is '工作描述';
comment on column experience.salary is '薪水';
/*========================个人简历管理系统end========================*/
