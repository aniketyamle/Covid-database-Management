#code to connect mysql server to upload csv data
import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
    print("SQL Server Connected")
except Error as e:
    print("Error ", e)


import pandas as pd
cursor=conn.cursor()
#inserting state table
statedata = pd.read_csv('/Users/aniketyamle/Us_state.csv', index_col=False, delimiter = ',')

for i,row in statedata.iterrows():
    sql="INSERT INTO State(State_id,State, Abbreviation , YearOfStatehood,Capital,Capital_Since,LandArea ,IsPopulousCity ,MunicipalPopulation,MetroPopulation) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"   
    cursor.execute(sql,tuple(row))
conn.commit()
print("State record inserted")


countydata = pd.read_csv('/Users/aniketyamle/Us_county.csv', index_col=False, delimiter = ',')
print(countydata)
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
for j,row2 in countydata.iterrows():
    #print(row2)
    sql2="INSERT INTO county(State,County , Population,Latitude,Longitude) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql2,tuple(row2))
conn.commit()
print("record inserted")


vaccinationdata = pd.read_csv('/Users/aniketyamle/Us_Vaccination.csv', index_col=False, delimiter = ',')
print(vaccinationdata)
for i,row in vaccinationdata.iterrows():
    #print(row)
    sql5="INSERT INTO Vaccinations(State,TotalDistributed ,TotalAdministered ,Distributed_per_100K ,Administered_per_100K ,MoreThanOneDoses ,MoreThanOneDosesPer100K ,Two_Doses ,MoreThanTwoDosesPer100K ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #print(sql)
    cursor.execute(sql5,tuple(row))
    #print("record inserted")
conn.commit()
print("VACCINATIONS record inserted")



#code to connect mysql server to upload csv data
import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
    print("SQL Server Connected")
except Error as e:
    print("Error ", e)
    
import pandas as pd
cursor=conn.cursor()
#converting deaths data table

deathsdata = pd.read_csv('/Users/aniketyamle/Us_deaths.csv', index_col=False, delimiter = ',',low_memory=False)
deathsdata.head()
df=pd.DataFrame(deathsdata)
#casesdata = casesdata.reset_index()
df = pd.melt(df,id_vars=['Province_State','County'], var_name='ReportDate', value_name='DeathCount')
df=df.fillna(0)
import csv
df.to_csv("death.csv")


dff = pd.read_csv('/Users/aniketyamle/death.csv', parse_dates=['ReportDate'])
#print(dff)
del dff[dff.columns[0]]
print(dff)
import csv
dff.to_csv("updeath.csv",index=False)




import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
    print("SQL Server Connected")
except Error as e:
    print("Error ", e)
    
import pandas as pd
cursor=conn.cursor()

#converting confirmed cases data table
casesdata = pd.read_csv('/Users/aniketyamle/Us_confirmed_cases.csv', index_col=False, delimiter = ',',low_memory=False)
casesdata.head()
cases=pd.DataFrame(casesdata)
#casesdata = casesdata.reset_index()
cases = pd.melt(cases,id_vars=['Province_State','County'], var_name='TestDate', value_name='Positivecount')
cases=cases.fillna(0)
print(cases)

import csv
cases.to_csv("cases.csv")



cc = pd.read_csv('/Users/aniketyamle/cases.csv', parse_dates=['TestDate'])
#print(dff)
del cc[cc.columns[0]]
print(cc)
import csv
cc.to_csv("upcases.csv",index=False)



