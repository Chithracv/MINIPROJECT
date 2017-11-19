drop table if exists student;
create table student( Roll_no varchar(20), Name varchar(20), Class varchar(20), Password varchar(20), primary key(Roll_no, Class));

drop table if exists act;
create table act( Aid int,Activity varchar(20), Activity_level varchar(20) default 'No Level', Point int, primary key(Activity,Activity_level,Point));

drop table if exists faculty;
create table faculty( Fac_id varchar(20), Password varchar(20));

drop table if exists StudAct;
create table StudAct( Roll_no varchar(20), Aid int, foreign key(Roll_no) references Student(Roll_no),foreign key(Aid) references Act(Aid));




