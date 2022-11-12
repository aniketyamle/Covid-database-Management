1.Connected to Mysql server

    Created a creation.sql file to execute all create table statements for state,county,confirmed_cases,deathss and vaccinations.
    Output file of creation.sql is tablescreated .

2.To upload csv data of state,county, vaccinations:
  		Connected to server using python code and performed insertion of queries.
  		Programming code is saved to code.py file
  		Output displayed in codeforuploading data.html

  		Code executed in jupyter notebook in form block of code execution.


	    To upload csv data of deaths,confirmed cases
  		code.py contains formatting of confirmed cases ,deathss to proper format into csv file.
  		Output file:formatting confirmed cases data.html
  			 	    death_table formatting.html


  		code2.py file and code3.py contains code for insertion queries of deathss and confirmed_cases.
  	# as one time insertion of 12Lakh records taking more than 6+ hours to complete the query.
  	## Divided csv into multiple small csv files and performed insertion into multiple parallel sessions of server.


3.Executed all query objectives except 7 and 8 where data of vaccination is not 
 	given  per county .So it is not possible to run those queries.
 	Filename:queries


4.Performed insert violation and captured all statment into spool file.
	File:insertviolation


5.Performed delte violation queries.
  File: deleteviolations.txt

6.Performed Insertion of queries into tables.
  Filename:insertwithoutviolation.txt


#Data of tables attached i.e. tables data
State : File statedata
County : Countydata
Cases :casesdata
Vaccination :vaccinationdata



