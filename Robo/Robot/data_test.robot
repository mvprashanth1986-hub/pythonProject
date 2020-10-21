*** Settings ***
Library  SeleniumLibrary
Resource      ../Robo/Robot/Data_Driven.robot
Suite Setup       open bro
Suite Teardown    close bro
Test Template  Invalid Login

*** Test Cases ***              username                        password
right user empty password       mvprashanth1986@gmail.com       dfg
right user wrong password       mvprashanth1986@gmail.com       pass
Wrong user right password       mvprashanth19861@gmail.com      Moonshine@123
wrong user empty password       mvprashanth1986@gmail.com       fghfgh

*** Keywords ***
Invalid Login
    [Arguments]  ${username}    ${password}
    open page
    Input Username      ${username}
    Input Password      ${password}
    Click Login Button
    errror message

Valid Login
    [Arguments]  ${username}    ${password}
    open page
    Input Username      ${username}
    Input Password      ${password}
    Click Login Button
    positive message