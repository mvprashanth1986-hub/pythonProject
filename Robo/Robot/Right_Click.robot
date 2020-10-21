*** Settings ***

Library  SeleniumLibrary

*** Test Cases ***
Login
    open browser        http://www.seleniumframework.com/Practiceform/   Chrome
    set selenium speed  2 seconds
    click element   xpath://button[@id='button1']
    Maximize Browser Window



    close browser
