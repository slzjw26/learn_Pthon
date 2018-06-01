/*========================��˾Ա��нˮ����ϵͳstart========================*/
/*
    ��нˮ=����нˮ+����
    ��ϵ��
        1��employ.deptid = dept.deptid(ĳ��Ա������ĳ������)
        2��employ.stationid = station.stationid(ĳ��Ա����ĳ��������ְ�ĸ�λ)
        3��salary.employid = employ.employid(ĳ��Ա����н��)
*/
create table dept(
       deptid int, 
       deptname char(50)
);
alter table DEPT add constraint PK_DEPT primary key(DEPTID);
comment on table dept is '������Ϣ';
comment on column dept.deptid is '����ID';
comment on column dept.deptname is '��������';

create table station(
       stationid int,
       stationname char(50)
);
alter table STATION add constraint PK_STATION primary key (STATIONID);
comment on table station is '��λ��Ϣ';
comment on column station.stationid is '��λID';
comment on column station.stationname is '��λ����';

create table employ(
       employID int,
       ename char(50),
       sex char(50),
       age int,
       deptid int,
       stationid int
); 
alter table EMPLOY add constraint PK_EMPLOY primary key (EMPLOYID);
comment on table employ is 'Ա����Ϣ';
comment on column employ.employID is 'Ա��ID';
comment on column employ.ename is 'Ա������';
comment on column employ.sex is '�Ա�';
comment on column employ.age is '����';
comment on column employ.deptid is '����ID';
comment on column employ.stationid is '��λID';

create table salary(
       salaryid int,
       employid int,
       basesalary int,
       bonussalary int
);
alter table SALARY add constraint PK_salary primary key (SALARYID);
comment on table salary is 'Ա��нˮ';
comment on column salary.salaryid is 'нˮID';
comment on column salary.employid is 'Ա��ID';
comment on column salary.basesalary is '����нˮ';
comment on column salary.bonussalary is '����';
/*========================��˾Ա��нˮ����ϵͳend========================*/



/*========================���˼�������ϵͳstart========================*/
/*
    ��ϵ��
        1�� companystation.companyid = company.companyid(ĳ��������ĳ����˾��ְ��λ)
        2�� companystation.personid = person.personid(ĳ��������ĳ����˾��ְ��λ)
        3�� experience.companystationid = companystation.companystationid(ĳ����������ְ��˾�Ĺ�������)
*/
create table person(
       personID int,
       ename char(50),
       sex char(50),
       age int
); 
alter table PERSON add constraint PK_PERSON primary key (PERSONID);
comment on table person is '������Ϣ';
comment on column person.personID is '��ԱID';
comment on column person.ename is '����';
comment on column person.sex is '�Ա�';
comment on column person.age is '����';

create table company(
       companyid int,
       companyname char(50)
);
alter table COMPANY add constraint PK_COMPANY primary key (COMPANYID);
comment on table company is '������λ';
comment on column company.companyid is '��˾ID';
comment on column company.companyname is '��˾����';

create table companystation(
       companystationid int,
       companyid int,
       personid int,
       stationname char(50)
);
alter table COMPANYSTATION add constraint PK_COMPANYSTATION primary key (COMPANYSTATIONID);
comment on table companystation is '�������ڹ�˾�ĸ�λ';
comment on column companystation.companystationid is '�������ڹ�˾�ĸ�λID';
comment on column companystation.companyid is '��˾ID';
comment on column companystation.personid is '����ID';
comment on column companystation.stationname is '��λ����';

create table experience(
       experienceid int,
       companystationid int,
       startdate date,
       enddate date,
       descsr char(1000),
       salary int
);
alter table EXPERIENCE add constraint PK_EXPERIENCE primary key (EXPERIENCEID);
comment on table experience is '���˹�������';
comment on column experience.experienceid is '����ID';
comment on column experience.companystationid is '�������ڹ�˾�ĸ�λID';
comment on column experience.startdate is '������ʼ����';
comment on column experience.enddate is '������������';
comment on column experience.descsr is '��������';
comment on column experience.salary is 'нˮ';
/*========================���˼�������ϵͳend========================*/
