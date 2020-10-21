*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://www.freelancer.in/
${browser}  Chrome


*** Test Cases ***
Login Test
    set selenium speed      3 seconds
    login
    close browser


*** Keywords ***

Login
    open browser     ${url}     ${browser}
    click link       Log In
    input text      xpath://input[@type='email']  mvprashanth1986@gmail.com
    input text      xpath://input[@type='password']   Sunshine@1
    click element     xpath://button[@type='submit']



