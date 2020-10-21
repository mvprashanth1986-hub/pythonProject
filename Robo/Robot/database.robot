*** Settings ***
Library  DatabaseLibrary
Library  OperatingSystem

Suite Setup     Connect To Database     pymysql     ${dbname}   ${dbuser}   ${dbpassword}   ${dbhost}   ${dbport}
Suite Teardown  Disconnect From Database

*** Variables ***
${dbname}   mydb
${dbuser}   root
${dbpassword}   root
${dbhost}   127.0.0.1
${dbport}   3306

*** Test Cases ***
Data Insertion
    ${output} =  Execute SQL String      select * from studens
    should be equal as strings      ${output}       None
    ${output} =  Execute SQL Script     ./testdata/Test.sql

Check data record exists
    check if exists in database     select id from mydb.person where name='David'

Check data record doesnot exists
    check if exists in database     select id from mydb.person where name='David1'

Check table exists or not
    table must exists       Student

Verify row count
    row count is 0      select name from Students where id='102'
    row count is equal to x     select * from Students where name='John'

Update record
    ${output}=  Execute SQL String      update mydb.person set name="Johny" where id='203'
    should be equal as strings      ${output}       None

Retrive records
    ${queryresult}=  query   select * from mydb.person
    log to console      many    ${queryresult}


