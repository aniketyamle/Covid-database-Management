#Splitted deaths data into multi csv files for fast insertion of queries
#Parallel execution of queries in different sessions
# used for cases data

import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d1 = pd.read_csv('/Users/aniketyamle/upcases/upcases-1.csv', index_col=False, delimiter = ',')
for i,row in d1.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

#-------------------------------------------------------------------------------------------

import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d2 = pd.read_csv('/Users/aniketyamle/upcases/upcases-2.csv', index_col=False, delimiter = ',')
for i,row in d2.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

#-------------------------------------------------------------------------------------------


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d3 = pd.read_csv('/Users/aniketyamle/upcases/upcases-3.csv', index_col=False, delimiter = ',')
for i,row in d3.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

#-------------------------------------------------------------------------------------------


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d4 = pd.read_csv('/Users/aniketyamle/upcases/upcases-4.csv', index_col=False, delimiter = ',')
for i,row in d4.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted"


#-------------------------------------------------------------------------------------------

import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d5 = pd.read_csv('/Users/aniketyamle/upcases/upcases-5.csv', index_col=False, delimiter = ',')
for i,row in d5.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

#-------------------------------------------------------------------------------------------


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d6 = pd.read_csv('/Users/aniketyamle/upcases/upcases-6.csv', index_col=False, delimiter = ',')
for i,row in d6.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

#-------------------------------------------------------------------------------------------


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d7 = pd.read_csv('/Users/aniketyamle/upcases/upcases-7.csv', index_col=False, delimiter = ',')
for i,row in d7.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

#-------------------------------------------------------------------------------------------


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d8 = pd.read_csv('/Users/aniketyamle/upcases/upcases-8.csv', index_col=False, delimiter = ',')
for i,row in d8.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

#-------------------------------------------------------------------------------------------


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d9 = pd.read_csv('/Users/aniketyamle/upcases/upcases-9.csv', index_col=False, delimiter = ',')
for i,row in d9.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")


#-------------------------------------------------------------------------------------------


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d10 = pd.read_csv('/Users/aniketyamle/upcases/upcases-10.csv', index_col=False, delimiter = ',')
for i,row in d10.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

#-------------------------------------------------------------------------------------------



import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d11 = pd.read_csv('/Users/aniketyamle/upcases/upcases-11.csv', index_col=False, delimiter = ',')
for i,row in d11.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")


#-------------------------------------------------------------------------------------------

import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d12 = pd.read_csv('/Users/aniketyamle/upcases/upcases-12.csv', index_col=False, delimiter = ',')
for i,row in d12.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")


#-------------------------------------------------------------------------------------------

import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d13 = pd.read_csv('/Users/aniketyamle/upcases/upcases-13.csv', index_col=False, delimiter = ',')
for i,row in d13.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

#-------------------------------------------------------------------------------------------


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d14 = pd.read_csv('/Users/aniketyamle/upcases/upcases-14.csv', index_col=False, delimiter = ',')
for i,row in d14.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

#-------------------------------------------------------------------------------------------


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d15 = pd.read_csv('/Users/aniketyamle/upcases/upcases-15.csv', index_col=False, delimiter = ',')
for i,row in d15.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")
#-------------------------------------------------------------------------------------------



import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d16 = pd.read_csv('/Users/aniketyamle/upcases/upcases-16.csv', index_col=False, delimiter = ',')
for i,row in d16.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")


#-------------------------------------------------------------------------------------------

import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d17 = pd.read_csv('/Users/aniketyamle/upcases/upcases-17.csv', index_col=False, delimiter = ',')
for i,row in d17.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

#-------------------------------------------------------------------------------------------


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d18 = pd.read_csv('/Users/aniketyamle/upcases/upcases-18.csv', index_col=False, delimiter = ',')
for i,row in d18.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

#-------------------------------------------------------------------------------------------


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d19 = pd.read_csv('/Users/aniketyamle/upcases/upcases-19.csv', index_col=False, delimiter = ',')
for i,row in d19.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

#-------------------------------------------------------------------------------------------


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d20 = pd.read_csv('/Users/aniketyamle/upcases/upcases-20.csv', index_col=False, delimiter = ',')
for i,row in d20.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

#-------------------------------------------------------------------------------------------


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d21 = pd.read_csv('/Users/aniketyamle/upcases/upcases-21.csv', index_col=False, delimiter = ',')
for i,row in d21.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

#-------------------------------------------------------------------------------------------


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d22 = pd.read_csv('/Users/aniketyamle/upcases/upcases-22.csv', index_col=False, delimiter = ',')
for i,row in d22.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

#-------------------------------------------------------------------------------------------


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d23 = pd.read_csv('/Users/aniketyamle/upcases/upcases-23.csv', index_col=False, delimiter = ',')
for i,row in d23.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

#-------------------------------------------------------------------------------------------


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='acadmysqldb001p.uta.edu', database='axy9230',user='axy9230',password="ANIYAM25$$");
except Error as e:
    print("Error", e)
    
import pandas as pd
cursor=conn.cursor()
cursor.execute("SET SESSION MAX_EXECUTION_TIME=2000")
cursor.execute("SET SESSION sql_mode='NO_AUTO_VALUE_ON_ZERO';")
d24 = pd.read_csv('/Users/aniketyamle/upcases/upcases-24.csv', index_col=False, delimiter = ',')
for i,row in d24.iterrows():
    #print(row)
    sql1="INSERT INTO confirmed_cases(State,County,TestDate, PositiveCount) VALUES (%s,%s,%s,%s)"    
    #print(sql)
    cursor.execute(sql1,tuple(row))
    #print("record inserted")
conn.commit()
print("record inserted")

