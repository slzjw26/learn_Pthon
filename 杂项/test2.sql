A:
select S#, GRADE from SC
where C# = 'C2';

B:
select sname from S
where sname like 'D%';

C:
select S.sname, S.S# from S, SC, C
where C.C# = SC.C# and SC.S# = S.S# and C.CNAME = 'Maths';

D:
select SC.S# from SC, C
where C.C# = SC.C# and C.C# in ('C2', 'C4');