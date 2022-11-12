CREATE TABLE State 
(State_id int NOT NULL,
 State char(50) ,
 Abbreviation char(2) NOT NULL,
 YearOfStatehood int NOT NULL,
 Capital char(50) NOT NULL,
 Capital_Since int NOT NULL,
 LandArea decimal NOT NULL,
 IsPopulousCity char(3) NOT NULL,
 MunicipalPopulation int ,
 MetroPopulation int ,
 Primary Key (State));

CREATE TABLE County 
(State Varchar (50), 
 County Varchar (50),
 Population int,
 Latitude decimal(10,8) ,
 Longitude decimal(10,8),
 Primary Key (State,County),
 Foreign Key (State) references State(State));

CREATE TABLE CONFIRMED_CASES 
(State Varchar (50), 
County Varchar (50),
TestDate date,
PositiveCount int,
Foreign Key (State) references State(State) ,
Primary Key (State,County,TestDate));

CREATE TABLE DEATHSS 
(State Varchar (50), 
County Varchar (50), 
ReportDate date,
DeathCount int ,
Foreign Key (State) references State(State),
Primary Key (State,County,ReportDate));

CREATE TABLE VACCINATIONS 
(State Varchar (50),
TotalDistributed int,
TotalAdministered int,
Distributed_per_100K int,
Administered_per_100K int,
MoreThanOneDoses int,
MoreThanOneDosesPer100K int,
Two_Doses int,
MoreThanTwoDosesPer100K int,
Foreign Key (State) references State(State));

