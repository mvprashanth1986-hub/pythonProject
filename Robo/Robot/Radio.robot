*** Settings ***

Library  SeleniumLibrary

*** Test Cases ***
Login
    open browser        http://www.practiceselenium.com/practice-form.html    Chrome
    #set selenium speed  1 seconds
    input text  name:firstname     James
    input text  name:lastname      Bond
    input text  id:datepicker      34535
    select radio button     sex     Female
    select radio button     exp     3
    select checkbox     Black Tea
    select checkbox     Break
    Select From List By Label   continents   Australia
    Select From List By Label   continents   Asia
    Select From List By Index   continents   5
    Select From List By Label   selenium_commands   Browser Commands
    Select From List By Label   selenium_commands   Navigation Commands
    Select From List By Index   selenium_commands   3


