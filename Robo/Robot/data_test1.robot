*** Settings ***
Library  SeleniumLibrary
Resource      ../Robo/Robot/Data_Driven.robot
Library        DataDriver
Suite Setup       open bro
Suite Teardown    close bro
Test Template  Invalid Login

*** Test Cases ***
logintestwithxl using       ${username}     ${password}

*** Keywords ***
Invalid Login
    [Arguments]  ${username}    ${password}
    open page
    Input Username      ${username}
    Input Password      ${password}
    Click Login Button
    errror message

#Valid Login
#    [Arguments]  ${username}    ${password}
#    open page
#    Input Username      ${username}
#    Input Password      ${password}
#    Click Login Button
#    positive message