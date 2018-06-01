/*========================��˾Ա��нˮ����ϵͳstart========================*/
--��������
insert into DEPT (deptid, deptname) values (1, '������');
insert into DEPT (deptid, deptname) values (2, '�г���');
commit;

--��λ����
insert into STATION (stationid, stationname) values (1, '���۾���');
insert into STATION (stationid, stationname) values (2, '����Ա');
insert into STATION (stationid, stationname) values (3, '��������');
insert into STATION (stationid, stationname) values (4, '��������ʦ');
commit;

--Ա������
insert into EMPLOY (employid, ename, sex, age, deptid, stationid)
values (1, '��ϼ��', '��', 31, 1, 4);
insert into EMPLOY (employid, ename, sex, age, deptid, stationid)
values (2, '����', 'Ů', 20, 1, 1);
insert into EMPLOY (employid, ename, sex, age, deptid, stationid)
values (3, '����', '��', 34, 2, 2);
insert into EMPLOY (employid, ename, sex, age, deptid, stationid)
values (4, '����', 'Ů', 28, 2, 3);
insert into EMPLOY (employid, ename, sex, age, deptid, stationid)
values (5, '����', '��', 45, 1, 4);
insert into EMPLOY (employid, ename, sex, age, deptid, stationid)
values (6, '��С��', 'Ů', 56, 1, 2);
insert into EMPLOY (employid, ename, sex, age, deptid, stationid)
values (7, '��С��', '��', 21, 2, 3);
insert into EMPLOY (employid, ename, sex, age, deptid, stationid)
values (8, '��С', '��', 19, 2, 4);
insert into EMPLOY (employid, ename, sex, age, deptid, stationid)
values (9, '�̲�', 'Ů', 27, 1, 1);
insert into EMPLOY (employid, ename, sex, age, deptid, stationid)
values (10, '��', '��', 33, 1, 3);
commit;

--нˮ����
insert into SALARY (salaryid, employid, basesalary, bonussalary)
values (1, 1, 1000, 3000);
insert into SALARY (salaryid, employid, basesalary, bonussalary)
values (2, 2, 2200, 3100);
insert into SALARY (salaryid, employid, basesalary, bonussalary)
values (3, 3, 400, 2000);
insert into SALARY (salaryid, employid, basesalary, bonussalary)
values (4, 4, 300, 5000);
insert into SALARY (salaryid, employid, basesalary, bonussalary)
values (5, 5, 1700, 3456);
insert into SALARY (salaryid, employid, basesalary, bonussalary)
values (6, 6, 1800, 2345);
insert into SALARY (salaryid, employid, basesalary, bonussalary)
values (7, 7, 1900, 2189);
insert into SALARY (salaryid, employid, basesalary, bonussalary)
values (8, 8, 1200, 3456);
insert into SALARY (salaryid, employid, basesalary, bonussalary)
values (9, 9, 2600, 7642);
insert into SALARY (salaryid, employid, basesalary, bonussalary)
values (10, 10, 3400, 2155);
commit;
/*========================��˾Ա��нˮ����ϵͳend========================*/

/*========================���˼�������ϵͳstart========================*/
--������λ����
insert into COMPANY (companyid, companyname)
values (1, 'ORACLE');
insert into COMPANY (companyid, companyname)
values (2, 'IBM');
commit;

--������Ϣ����
insert into PERSON (personid, ename, sex, age)
values (1, '��ϼ��', '��', 31);
insert into PERSON (personid, ename, sex, age)
values (2, '����', 'Ů', 20);
insert into PERSON (personid, ename, sex, age)
values (3, '����', '��', 34);
insert into PERSON (personid, ename, sex, age)
values (4, '����', 'Ů', 28);
insert into PERSON (personid, ename, sex, age)
values (5, '����', '��', 45);
insert into PERSON (personid, ename, sex, age)
values (6, '��С��', 'Ů', 56);
insert into PERSON (personid, ename, sex, age)
values (7, '��С��', '��', 21);
insert into PERSON (personid, ename, sex, age)
values (8, '��С', '��', 19);
insert into PERSON (personid, ename, sex, age)
values (9, '�̲�', 'Ů', 27);
insert into PERSON (personid, ename, sex, age)
values (10, '��', '��', 33);
commit;

--���˹�����λ��λ����
insert into COMPANYSTATION (companystationid, companyid, personid, stationname)
values (1, 1, 1, '���Թ���ʦ');
insert into COMPANYSTATION (companystationid, companyid, personid, stationname)
values (2, 2, 2, '��������ʦ');
insert into COMPANYSTATION (companystationid, companyid, personid, stationname)
values (3, 1, 3, '���Թ���ʦ');
insert into COMPANYSTATION (companystationid, companyid, personid, stationname)
values (4, 1, 4, '��������ʦ');
insert into COMPANYSTATION (companystationid, companyid, personid, stationname)
values (5, 2, 5, '��������ʦ');
insert into COMPANYSTATION (companystationid, companyid, personid, stationname)
values (6, 2, 6, '��������ʦ');
insert into COMPANYSTATION (companystationid, companyid, personid, stationname)
values (7, 2, 7, '���Թ���ʦ');
insert into COMPANYSTATION (companystationid, companyid, personid, stationname)
values (8, 1, 8, '��������ʦ');
insert into COMPANYSTATION (companystationid, companyid, personid, stationname)
values (9, 1, 9, '��������ʦ');
insert into COMPANYSTATION (companystationid, companyid, personid, stationname)
values (10, 1, 10, '���Թ���ʦ');
insert into COMPANYSTATION (companystationid, companyid, personid, stationname)
values (11, 1, 2, '���Թ���ʦ');
commit;

--������������
insert into EXPERIENCE (experienceid, companystationid, startdate, enddate, descsr, salary)
values (1, 1, to_date('12-05-2009', 'dd-mm-yyyy'), to_date('16-05-2010', 'dd-mm-yyyy'), 'xxx', 3000);
insert into EXPERIENCE (experienceid, companystationid, startdate, enddate, descsr, salary)
values (2, 2, to_date('12-05-2010', 'dd-mm-yyyy'), to_date('16-05-2012', 'dd-mm-yyyy'), 'ccc', 4000);
insert into EXPERIENCE (experienceid, companystationid, startdate, enddate, descsr, salary)
values (3, 3, to_date('12-05-2009', 'dd-mm-yyyy'), to_date('16-05-2013', 'dd-mm-yyyy'), 'aa', 5000);
insert into EXPERIENCE (experienceid, companystationid, startdate, enddate, descsr, salary)
values (4, 4, to_date('12-05-2008', 'dd-mm-yyyy'), to_date('16-05-2010', 'dd-mm-yyyy'), 'bb', 4323);
insert into EXPERIENCE (experienceid, companystationid, startdate, enddate, descsr, salary)
values (5, 5, to_date('12-05-2007', 'dd-mm-yyyy'), to_date('16-05-2010', 'dd-mm-yyyy'), 'cc', 5453);
insert into EXPERIENCE (experienceid, companystationid, startdate, enddate, descsr, salary)
values (6, 6, to_date('12-05-2009', 'dd-mm-yyyy'), to_date('16-05-2010', 'dd-mm-yyyy'), 'dd', 3243);
insert into EXPERIENCE (experienceid, companystationid, startdate, enddate, descsr, salary)
values (7, 7, to_date('12-05-2010', 'dd-mm-yyyy'), to_date('16-05-2013', 'dd-mm-yyyy'), 'fff', 3654);
insert into EXPERIENCE (experienceid, companystationid, startdate, enddate, descsr, salary)
values (8, 8, to_date('12-05-2011', 'dd-mm-yyyy'), to_date('16-05-2013', 'dd-mm-yyyy'), 'dfadsfd', 4543);
insert into EXPERIENCE (experienceid, companystationid, startdate, enddate, descsr, salary)
values (9, 9, to_date('12-05-2012', 'dd-mm-yyyy'), to_date('16-05-2013', 'dd-mm-yyyy'), 'fdsf', 5435);
insert into EXPERIENCE (experienceid, companystationid, startdate, enddate, descsr, salary)
values (10, 10, to_date('12-05-2009', 'dd-mm-yyyy'), to_date('16-05-2010', 'dd-mm-yyyy'), 'dsfdsf', 4535);
insert into EXPERIENCE (experienceid, companystationid, startdate, enddate, descsr, salary)
values (11, 11, to_date('16-05-2010', 'dd-mm-yyyy'), to_date('16-05-2013', 'dd-mm-yyyy'), 'ds', 4534);
commit;
/*========================���˼�������ϵͳend========================*/
