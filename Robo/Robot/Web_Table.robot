*** Settings ***
Library  SeleniumLibrary


*** Test Cases ***
case
    open browser  http://testautomationpractice.blogspot.com/   chrome
    Maximize Browser Window
    set selenium speed   2 seconds
    ${row_count}=   get element count     xpath://table[@name='BookTable']/tbody/tr
    ${col_count}=  get element count      xpath://table[@name='BookTable']/tbody/tr/th
    log to console  ${row_count}
    log to console  ${col_count}

    ${data}=  get text  xpath://table[@name='BookTable']/tbody/tr[4]/td[3]
    log to console  ${data}

    table column should contain     xpath://table[@name='BookTable']    1   BookName
    table row should contain     xpath://table[@name='BookTable']    2   Learn Selenium
    table cell should contain   xpath://table[@name='BookTable']    5   2   Mukesh
    table header should contain   xpath://table[@name='BookTable']      BookName